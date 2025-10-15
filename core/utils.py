from contextlib import contextmanager
from InquirerPy.prompts.fuzzy import FuzzyPrompt
from InquirerPy.prompts.confirm import ConfirmPrompt
from InquirerPy.prompts.input import InputPrompt
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


@contextmanager
def retry(max_attempts: int):
    """A context manager for retrying a block of code up to max_attempts times.

    Usage:
        with retry(3) as attempt:
            print(f"Attempt {attempt}")
            do_work()
    """
    attempt = 1
    while True:
        try:
            yield attempt
            break
        except Exception as e:
            if attempt >= max_attempts:
                typer.echo(f"Error: Maximum attempts reached: {e}")
                raise typer.Exit(code=1)
            attempt += 1
            typer.echo(f"Warning: Attempt {attempt - 1} failed: {e}. Retrying...")

def autocomplete(prompt: str, options: List[str], default: str = "") -> str:
    """Prompt the user with an autocomplete input."""
    return FuzzyPrompt(
        message=prompt,
        choices=options,
        default=default,
    ).execute()

def confirm(prompt: str, default: bool = False) -> bool:
    return ConfirmPrompt(message=prompt, default=default).execute()

def prompt(prompt: str, default: str = "") -> str:
    return InputPrompt(message=prompt, default=default).execute()
