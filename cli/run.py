import typer
from core import utils, commands
from core.problems import Problems

def main(slug = typer.Argument("", help="Leetcode problem slug (search if not provided)")) -> None:
    """
    Run a Leetcode problem by slug or via search
    """
    problems = Problems()
    ids = problems.list_ids()
    if not slug or any(id != slug and id.startswith(slug) for id in ids):
        partial = slug if slug else ""
        slug = utils.autocomplete("Select a problem to run: ", problems.list_ids(), default=partial)

    if not problems.has_problem(slug):
        typer.echo(f"Problem '{slug}' not found.")
        return

    problem = problems.get_problem(slug)
    assert problem is not None

    code, stdout, stderr = commands.run(f"python3 {problem.directory}/solution.py")
    if code == 0:
        typer.echo(f"Problem '{slug}' ran successfully.")
        typer.echo(stdout)
    else:
        typer.echo(f"Error running problem '{slug}':")
        typer.echo(stderr)
        raise typer.Exit(code=1)




