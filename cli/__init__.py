import typer
from . import add, run, remove, test

app = typer.Typer(help="Leetcode problem management CLI too.")

app.command(name="add", help="Create a new Leetcode problem testing and documentation environment")(add.main)
app.command(name="run", help="Run tests for a Leetcode problem")(run.main)
app.command(name="remove", help="Remove a Leetcode problem by slug or via search")(remove.main)
app.command(name="test", help="Test a Leetcode problem by slug or via search")(test.main)
