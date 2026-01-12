import typer
from typing import Optional
from playwright.sync_api import sync_playwright
from core import commands, templates
from core.problem_metadata import ProblemMetadata
from core.problems import Problems, Problem
from core.scraper import Scraper
from core.utils import spinner

VALID_DIFFICULTIES = ["Easy", "Medium", "Hard"]


def main(
    slug: Optional[str] = typer.Argument(None, help="Leetcode problem slug (e.g. two-sum)"),
    code_starter: str = typer.Option("class Solution:", "-s", "--starter", help="Provide what the code snippet should start with when scraping from Leetcode (defaults to 'class Solution:', useful for class based questions)"),
    custom: bool = typer.Option(False, "--custom", help="Create a custom problem (not from LeetCode) with interactive prompts")
) -> None:
    """
    Create a new problem from slug or custom input
    """
    if custom:
        __add_custom_problem()
    else:
        if not slug:
            typer.echo("Error: slug is required when not using --custom")
            raise typer.Exit(code=1)
        __add_leetcode_problem(slug, code_starter)


def __add_custom_problem() -> None:
    """Handle adding a custom problem via interactive prompts."""
    problems = Problems()
    
    # Prompt for problem details
    name = typer.prompt("Problem name")
    
    difficulty = typer.prompt(
        "Difficulty (Easy/Medium/Hard)",
        default="Medium"
    )
    if difficulty not in VALID_DIFFICULTIES:
        typer.echo(f"Error: Difficulty must be one of {VALID_DIFFICULTIES}")
        raise typer.Exit(code=1)
    
    function_def = typer.prompt(
        "Function definition (e.g. 'def twoSum(self, nums: List[int], target: int) -> List[int]:')"
    )
    
    # Validate function definition
    if not function_def.strip().startswith("def ") or "->" not in function_def:
        typer.echo("Error: Function definition must start with 'def ' and include a return type annotation '->'")
        raise typer.Exit(code=1)
    
    # Create metadata from custom input
    metadata = ProblemMetadata.from_custom(name, difficulty, function_def)
    
    # Check for collision
    if problems.has_problem(metadata.id):
        typer.echo(f"Error: Problem with id '{metadata.id}' already exists.")
        raise typer.Exit(code=1)
    
    # Create and populate files
    with spinner(f"Create files for '{metadata.id}'"):
        __create_problem_files(metadata)
    
    with spinner(f"Populate files for '{metadata.id}'"):
        __populate_files(metadata)
    
    with spinner(f"Add problem to JSON for '{metadata.id}'"):
        __save_to_json(problems, metadata)
    
    typer.echo(f"Created custom problem: {metadata.directory}/")


def __add_leetcode_problem(slug: str, code_starter: str) -> None:
    """Handle adding a LeetCode problem via scraping."""
    problems = Problems()
    
    # Step 1: Check if problem already exists in JSON
    if problems.has_problem(slug):
        typer.echo(f"Error: Problem with slug '{slug}' already exists.")
        raise typer.Exit(code=1)

    # Step 2: Fetch problem details via scraper with retries
    metadata = None
    for attempt in range(1, 4):
        try:
            with spinner(f"Fetch problem details for '{slug}' from LeetCode [Attempt {attempt}/3]"):
                metadata = __get_metadata(slug, code_starter)
            break
        except BaseException as e:
            if attempt >= 3:
                typer.echo(f"Error: Maximum attempts reached: {e}")
                raise typer.Exit(code=1)
            typer.echo(f"Warning: Attempt {attempt} failed. Retrying...")

    assert metadata is not None
    # Step 3: Create directory structure and files
    with spinner(f"Create files for '{metadata.id}'"):
        __create_problem_files(metadata)

    # Step 3: Populate files with templates and problem details
    with spinner(f"Populate files for '{metadata.id}'"):
        __populate_files(metadata)

    # Step 4: Add to `problems.json` with metadata
    with spinner(f"Add problem to JSON for '{metadata.id}'"):
        __save_to_json(problems, metadata)

def __get_metadata(slug: str, code_starter: str) -> ProblemMetadata:
    with sync_playwright() as playwright:
        scraper = Scraper(playwright)
        return scraper.extract_metadata(slug, code_starter)

def __create_problem_files(metadata: ProblemMetadata):
    commands.mkdir(metadata.directory)
    commands.touch(f"{metadata.directory}/docs.md")
    commands.touch(f"{metadata.directory}/notes.md")
    commands.touch(f"{metadata.directory}/solution.py")
    commands.touch(f"{metadata.directory}/tests.py")

def __populate_files(metadata: ProblemMetadata):
    templates.render_to_file("docs.md.j2", f"{metadata.directory}/docs.md", title=metadata.title, content=metadata.content_markdown())
    templates.render_to_file("solution.py.j2", f"{metadata.directory}/solution.py", problem_starter=metadata.problem_starter)
    parameter_names = metadata.parameter_names()
    if parameter_names:
        parameters_string = ", ".join(parameter_names)
    else:
        parameters_string = "COULD NOT PARSE PARMETERS, UPDATE MANUALLY"
    templates.render_to_file("tests.py.j2", f"{metadata.directory}/tests.py", 
        parameters=parameters_string,
        underscored_slug=metadata.id.replace("-", "_")
    )
    templates.render_to_file("notes.md.j2", f"{metadata.directory}/notes.md")

def __save_to_json(problems: Problems, metadata: ProblemMetadata):
    problem = Problem.base(metadata.id, metadata.title, metadata.directory, metadata.difficulty)
    problems.set_problem(problem)
    problems.save()



