from contextlib import contextmanager
from InquirerPy import inquirer
from typing import List
from yaspin import yaspin
import typer

OK = "✓ "
FAIL = "✗ "


def read_file(path: str) -> str:
    """Read the content of a file."""
    with open(path, 'r') as file:
        return file.read()


def write_file(path: str, content: str) -> None:
    """Write content to a file."""
    with open(path, 'w') as file:
        file.write(content)


@contextmanager
def spinner(text: str):
    """A context manager for displaying a spinner with standardized ok/fail handling.

    Usage:
        with spinner("Doing something"):
            do_work()

    On success, shows OK. On exception, shows FAIL and exits with code 1,
    printing: "Error: {text}: {e}".
    """
    with yaspin(text=text) as sp:
        try:
            yield sp
            sp.ok(OK)
        except Exception as e:
            sp.fail(FAIL)
            typer.echo(f"Error: {text}: {e}")
            raise typer.Exit(code=1)

def autocomplete(prompt: str, options: List[str], default: str = "") -> str:
    """Prompt the user with an autocomplete input."""
    return inquirer.fuzzy(
        message=prompt,
        choices=options,
        default=default,
    ).execute()

def confirm(prompt: str, default: bool = False) -> bool:
    return inquirer.confirm(message=prompt, default=default).execute()

def prompt(prompt: str, default: str = "") -> str:
    return inquirer.text(message=prompt, default=default).execute()
