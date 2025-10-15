import re
from typing import List
from markdownify import markdownify as md

class ProblemMetadata:
    def __init__(self, id: str, title: str, difficulty: str, content: str, problem_starter: str):
        self.id = id
        self.title = title
        self.problem_number = title.split(".")[0]
        self.directory = f"{self.problem_number}-{self.id}"
        self.difficulty = difficulty
        self.content = content
        self.problem_starter = problem_starter
        self.problem_starter = self.problem_starter.replace('\u00a0', ' ')     # nbsp
        self.problem_starter = self.problem_starter.replace('\xa0', ' ')       # sometimes shown as \xa0
        self.problem_starter = self.problem_starter.replace('\u200b', '')      # zero-width space

    def content_markdown(self) -> str:
        return md(self.content)

    def parameter_names(self) -> List[str] | None:
        pattern = r'def\s+\w+\s*\((.*?)\)\s*->'
        match = re.search(pattern, self.problem_starter, re.DOTALL)
        if match:
            arg_section = match.group(1)
            args = [arg.split(':')[0].strip() for arg in arg_section.split(',') if arg.strip()]
            filtered_args = [arg for arg in args if arg not in ('self', 'cls')]
            return filtered_args


    
