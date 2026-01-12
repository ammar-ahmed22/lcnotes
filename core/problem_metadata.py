import re
from typing import List
from markdownify import markdownify as md

class ProblemMetadata:
    def __init__(self, id: str, title: str, difficulty: str, content: str, problem_starter: str, directory: str | None = None):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.content = content
        self.problem_starter = problem_starter
        self.problem_starter = self.problem_starter.replace('\u00a0', ' ')     # nbsp
        self.problem_starter = self.problem_starter.replace('\xa0', ' ')       # sometimes shown as \xa0
        self.problem_starter = self.problem_starter.replace('\u200b', '')      # zero-width space
        
        # Directory: use provided value or derive from title (for LeetCode problems)
        if directory:
            self.directory = directory
        else:
            self.problem_number = title.split(".")[0]
            self.directory = f"{self.problem_number}-{self.id}"

    @classmethod
    def from_custom(cls, name: str, difficulty: str, function_def: str) -> "ProblemMetadata":
        """Create metadata for a custom problem (not from LeetCode)."""
        # Generate slug from name: lowercase, replace spaces with hyphens, remove non-alphanumeric
        slug = re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ', '-'))
        slug = re.sub(r'-+', '-', slug).strip('-')  # collapse multiple hyphens
        
        # Wrap function definition in class Solution
        problem_starter = f"class Solution:\n    {function_def}\n        pass"
        
        return cls(
            id=slug,
            title=name,
            difficulty=difficulty,
            content="",  # Empty content for custom problems
            problem_starter=problem_starter,
            directory=slug  # No number prefix for custom problems
        )

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


    
