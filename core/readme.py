from typing import List
from .problems import Problem, Problems
from . import templates

class README:
    def __init__(self):
        pass


    def __normalize_problems(self, problems: List[Problem]) -> List[Problem]:
        for problem in problems:
            problem.notes = problem.notes.replace("\n", "<br />")
        return problems

    def __sort_by_difficulty(self, problems: List[Problem]) -> List[Problem]:
        difficulty_order = {"Easy": 2, "Medium": 1, "Hard": 0}
        return sorted(problems, key=lambda p: difficulty_order.get(p.difficulty, 3))

    def generate(self, problems: Problems) -> str:
        """Generate README content based on the published problems."""
        published_problems = problems.published_problems()
        published_problems = self.__normalize_problems(published_problems)
        published_problems = self.__sort_by_difficulty(published_problems)
        colors = {
            "Easy": "green",
            "Medium": "orange",
            "Hard": "red"
        }
        return templates.render("README.md.j2", problems=published_problems, colors=colors)


