import typer
from core import utils, commands
from core.problems import Problems


def main(slug = typer.Argument("", help="Leetcode problem slug (search if not provided)")) -> None:
    """
    Remove a problem by slug or via search
    """
    problems = Problems()
    ids = problems.list_ids()
    if not slug or any(id.startswith(slug) for id in ids):
        partial = slug if slug else ""
        slug = utils.autocomplete("Select a problem to remove: ", problems.list_ids(), default=partial)

    if not problems.has_problem(slug):
        typer.echo(f"Problem '{slug}' not found.")
        return

    try:
        problems.remove_problem(slug)
        commands.rimraf(slug)
        problems.save()
        typer.echo(f"Problem '{slug}' removed successfully.")
    except Exception as e:
        typer.echo(f"Error removing problem '{slug}': {e}")
        raise typer.Exit(code=1)


