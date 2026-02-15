from typing import List, Tuple
from .problems import Problem, Problems
from . import templates

class README:
    def __init__(self):
        pass

    def __sort_by_difficulty(self, problems: List[Problem]) -> List[Problem]:
        difficulty_order = {"Easy": 2, "Medium": 1, "Hard": 0}
        return sorted(problems, key=lambda p: difficulty_order.get(p.difficulty, 3))

    def __count_difficulty(self, problems: List[Problem]) -> Tuple[int, int, int]:
        n_easy = len([p for p in problems if p.difficulty == "Easy"])
        n_med = len([p for p in problems if p.difficulty == "Medium"])
        n_hard = len([p for p in problems if p.difficulty == "Hard"])
        return (n_easy, n_med, n_hard)

    def generate(self, problems: Problems) -> str:
        """Generate README content based on the published problems."""
        published_problems = problems.published_problems()
        published_problems = self.__sort_by_difficulty(published_problems)
        n_easy, n_medium, n_hard = self.__count_difficulty(published_problems)
        colors = {
            "Easy": "green",
            "Medium": "orange",
            "Hard": "red"
        }
        return templates.render("README.md.j2", problems=published_problems, colors=colors, n_easy=n_easy, n_medium=n_medium, n_hard=n_hard)


