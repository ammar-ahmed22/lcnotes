import typer
from core import utils, commands
from core.problems import Problems

def main(slug = typer.Argument("", help="Leetcode problem slug (search if not provided)")) -> None:
    """
    Test Leetcode problem by slug or via search
    """
    problems = Problems()
    ids = problems.list_ids()
    if not slug or any(id != slug and id.startswith(slug) for id in ids):
        partial = slug if slug else ""
        slug = utils.autocomplete("Select a problem to test: ", problems.list_ids(), default=partial)

    if not problems.has_problem(slug):
        typer.echo(f"Problem '{slug}' not found.")
        return

    code, stdout, stderr = commands.run(f"python3 -m pytest {slug}/tests.py")
    if code == 0:
        typer.echo(f"Problem '{slug}' tests passed.")
        typer.echo(stdout)
    elif code == 1:
        typer.echo(f"Problem '{slug}' tests failed.")
        typer.echo(stdout)
        raise typer.Exit(code=1)
    else:
        typer.echo(f"Error running problem '{slug}':")
        typer.echo(stderr)
        raise typer.Exit(code=1)




