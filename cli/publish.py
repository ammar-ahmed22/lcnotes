import typer
from core import utils
from core.problems import Problems
from core.readme import README


def main(
    slug: str = typer.Argument(None, help="Leetcode problem slug (search through unpublished problems if not provided)"),
    all: bool = typer.Option(False, help="Publish all unpublished problems")
) -> None:
    """
    Publish problems to README and mark as published
    """
    problems = Problems()
    unpublished = problems.unpublished_problems()
    ids = [p.id for p in unpublished]
    
    if len(ids) == 0:
        typer.echo("No unpublished problems found.")
        return

    if all: # Publish all unpublished problems
        # will early return
        for id in ids:
            typer.echo(f"Publishing '{id}'")
            __publish_problem(problems, id)
            typer.echo(f"Successfully published '{id}'")
        return

    if not slug or any(id != slug and id.startswith(slug) for id in ids):
        partial = slug if slug else ""
        slug = utils.autocomplete("Select a problem to publish: ", ids, default=partial)
        # autocomplete search through unpublished problems
        pass

    __publish_problem(problems, slug)
    typer.echo(f"Successfully published '{slug}'")

def __publish_problem(problems: Problems, id: str):
    problem = problems.get_problem(id)
    if not problem:
        typer.echo(f"Problem '{id}' not found.")
        return

    if problem.published:
        typer.echo(f"Problem '{id}' is already published.")
        return
    

    # Extract notes
    notes = utils.read_file(f"./{id}/notes.md")

    add_tags = utils.confirm("Would you like to add tags to this problem?", default=True)

    tags = []
    if add_tags:
        tags_text = utils.prompt("Enter tags (comma-separated): ")
        tags = [tag.strip() for tag in tags_text.split(",") if tag.strip()]

    problem.tags = tags
    problem.notes = notes
    problem.publish()
    problems.set_problem(problem)

    readme = README()
    content = readme.generate(problems)
    utils.write_file("README.md", content)
    typer.echo("Updated README.md")

    problems.save()
    typer.echo("Updated problems.json")
