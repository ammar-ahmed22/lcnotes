import typer
from core import utils
from core.problems import Problems
from core.readme import README


def main() -> None:
    """
    Generate the README based on the current problems.json
    """
    problems = Problems()
    readme = README()
    content = readme.generate(problems)
    utils.write_file("README.md", content)
    typer.echo(f"Successfully generated README.md")
