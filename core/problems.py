from typing import List, Optional
from .utils import read_file, write_file
import json
from datetime import datetime as dt, timezone

class Problem:
    def __init__(self, id: str, title: str, directory: str, difficulty: str, tags: List[str], published: bool, datetime: Optional[str] = None):
        self.id = id
        self.title = title
        self.directory = directory
        self.difficulty = difficulty
        self.tags = tags
        self.published = published
        self.datetime = datetime

    @classmethod
    def from_dict(cls, problem: dict):
        if not all(k in problem for k in ("id", "title", "difficulty", "tags", "published", "datetime")):
            raise ValueError(f"problem: '{problem}' is invalid!")

        return cls(
            id=problem["id"],
            title=problem["title"],
            directory=problem["directory"],
            difficulty=problem["difficulty"],
            tags=problem["tags"],
            published=problem["published"],
            datetime=problem["datetime"]
        )

    @classmethod
    def base(cls, id: str, title: str, directory: str, difficulty: str):
        return cls(id, title, directory, difficulty, [], False, None)

    def publish(self):
        self.published = True
        self.datetime = dt.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    def unpublish(self):
        self.tags = []
        self.published = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "directory": self.directory,
            "difficulty": self.difficulty,
            "tags": self.tags,
            "published": self.published,
            "datetime": self.datetime
        }

class Problems:
    def __init__(self):
        try:
            content = read_file('problems.json').strip()
            if content == "":
                self.problems = {}
                self.__write_problems()
            else:
                self.problems = json.loads(content)
        except FileNotFoundError:
            # Initialize empty problems and create the file
            self.problems = {}
            self.__write_problems()

    def __write_problems(self):
        write_file('problems.json', json.dumps(self.problems, indent=4))

    def has_problem(self, id: str) -> bool:
        return id in self.problems

    def get_problem(self, id: str) -> Problem | None:
        problem = self.problems.get(id)
        if problem:
            return Problem.from_dict(problem)

    def set_problem(self, problem: Problem):
        self.problems[problem.id] = problem.to_dict()

    def save(self):
        self.__write_problems()

    def list_ids(self) -> List[str]:
        return list(self.problems.keys())

    def remove_problem(self, id: str) -> bool:
        if id in self.problems:
            del self.problems[id]
            return True
        return False
    
    def unpublished_problems(self) -> List[Problem]:
        return [Problem.from_dict(self.problems[problem]) for problem in self.problems if not self.problems[problem]["published"]]
    
    def published_problems(self) -> List[Problem]:
        return [Problem.from_dict(self.problems[problem]) for problem in self.problems if self.problems[problem]["published"]]




