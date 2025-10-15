import typer
from playwright.sync_api import sync_playwright
from core import commands, templates
from core.problem_metadata import ProblemMetadata
from core.problems import Problems, Problem
from core.scraper import Scraper
from core.utils import spinner


def main(slug = typer.Argument(help="Leetcode problem slug (e.g. two-sum)")) -> None:
    """
    Create a new problem from slug
    """
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
                metadata = __get_metadata(slug)
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

def __get_metadata(slug: str) -> ProblemMetadata:
    with sync_playwright() as playwright:
        scraper = Scraper(playwright)
        return scraper.extract_metadata(slug)

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



