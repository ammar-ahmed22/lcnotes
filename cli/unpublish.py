import typer
from core import utils
from core.problems import Problems
from core.readme import README


def main(
    slug: str = typer.Argument(None, help="Leetcode problem slug (search through published problems if not provided)"),
) -> None:
    """
    Publish problems to README and mark as published
    """
    problems = Problems()
    published = problems.published_problems()
    ids = [p.id for p in published]
    
    if len(ids) == 0:
        typer.echo("No published problems found.")
        return

    if not slug or any(id != slug and id.startswith(slug) for id in ids):
        partial = slug if slug else ""
        slug = utils.autocomplete("Select a problem to unpublish: ", ids, default=partial)
        # autocomplete search through unpublished problems
        pass

    __unpublish_problem(problems, slug)
    typer.echo(f"Successfully unpublished '{slug}'")

def __unpublish_problem(problems: Problems, id: str):
    problem = problems.get_problem(id)
    if not problem:
        typer.echo(f"Problem '{id}' not found.")
        return

    if not problem.published:
        typer.echo(f"Problem '{id}' is not published.")
        return
    

    problem.unpublish()
    problems.set_problem(problem)

    readme = README()
    content = readme.generate(problems)
    utils.write_file("README.md", content)
    typer.echo("Updated README.md")

    problems.save()
    typer.echo("Updated problems.json")
