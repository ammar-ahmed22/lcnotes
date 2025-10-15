import typer
from . import add, run, remove, test, publish, unpublish, generate_readme

app = typer.Typer(help="Leetcode problem management CLI too.")

app.command(name="add", help="Create a new Leetcode problem testing and documentation environment")(add.main)
app.command(name="run", help="Run tests for a Leetcode problem")(run.main)
app.command(name="remove", help="Remove a Leetcode problem by slug or via search")(remove.main)
app.command(name="test", help="Test a Leetcode problem by slug or via search")(test.main)
app.command(name="publish", help="Publish a Leetcode problem by slug or via search")(publish.main)
app.command(name="unpublish", help="Unpublish a Leetcode problem by slug or via search")(unpublish.main)
app.command(name="generate-readme", help="Generate the README.md based on the current problems.json")(generate_readme.main)
