from typing import List
from .utils import read_file, write_file
import json

class Problem:
    def __init__(self, id: str, title: str, difficulty: str, tags: List[str], notes: str, published: bool):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.tags = tags
        self.notes = notes
        self.published = published

    @classmethod
    def from_dict(cls, problem: dict):
        if not all(k in problem for k in ("id", "title", "difficulty", "tags", "notes", "published")):
            raise ValueError(f"problem: '{problem}' is invalid!")

        return cls(
            id=problem["id"],
            title=problem["title"],
            difficulty=problem["difficulty"],
            tags=problem["tags"],
            notes=problem["notes"],
            published=problem["published"]
        )

    @classmethod
    def base(cls, id: str, title: str, difficulty: str):
        return cls(id, title, difficulty, [], "", False)

    def publish(self):
        self.published = True

    def unpublish(self):
        self.notes = ""
        self.tags = []
        self.published = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "difficulty": self.difficulty,
            "tags": self.tags,
            "notes": self.notes,
            "published": self.published
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





