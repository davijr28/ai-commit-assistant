import typer
import pycountry
import os
from rich.console import Console
from rich.prompt import Prompt
from help import show_language_help, show_api_help, show_git_tutorial
from git_utils import get_git_diff, apply_commit
from llm import generate_commit
from typing import Optional

app = typer.Typer(help="AI Commit Message Generator")
console = Console()


# Validate and convert language input
def validate_lang(value: str):
    query = value.strip().lower()
    language = pycountry.languages.get(alpha_2=query) or pycountry.languages.get(
        name=query.capitalize()
    )
    if language and hasattr(language, "alpha_2"):
        return language.name
    return None


# Command to generate the commit message
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    language: Optional[str] = typer.Argument(
        None, help="Language code (e.g., 'pt'). Leave blank for English."
    ),
):
    # If no language specified, then default to English
    if language is None:
        language = "en"

    # Check if user asked for help
    elif language == "help":
        return help_menu()

    # Validate the language
    target_lang = validate_lang(language)
    if not target_lang:
        console.print(
            f"[yellow]Warning:[/yellow] '{language}' not recognized. Please, check [italic]python main.py help[/italic] to know more about language support."
        )
        raise typer.Exit()

    # Check staged changes
    diff = get_git_diff()
    if not diff.strip():
        console.print(
            f"[yellow]Warning:[/yellow] No staged changes found. Please, check [italic]python main.py help[/italic] to see Git basics for this tool."
        )
        raise typer.Exit()

    # Check if API key is set
    if not os.getenv("GEMINI_API_KEY"):
        console.print(
            f"[bold red]Error: Gemini API Key not found.[/bold red] Please, check [italic]python main.py help[/italic] to see the API setup instructions."
        )
        raise typer.Exit()

    with console.status(f"[bold green]Generating {target_lang} commit..."):
        message = generate_commit(diff, target_lang)

    if not message:
        console.print(
            "[bold red]Failed to connect to Gemini. Please, check your API key and connection.[/bold red]"
        )
        raise typer.Exit()

    console.print(
        f"\n[bold]Suggested commit message ({target_lang}):[/bold] [green]{message}[/green]"
    )

    if apply_commit(message):
        console.print(f"[bold blue]✓ Committed successfully![/bold blue]")


# --- Help Menu ---


@app.command(name="help")
def help_menu():
    """Interactive help menu for Languages, API, or Git."""
    console.print(f"\n[bold cyan]Main Help Menu[/bold cyan]")
    console.print(f"1. [bold]lang[/bold] - Supported languages")
    console.print(
        f"2. [bold]api[/bold]  - How to setup your [bold].env[/bold] file with Gemini API key"
    )
    console.print(f"3. [bold]git[/bold]  - Quick Git essentials for this tool")
    console.print(f"q. [bold]quit[/bold] - Exit help")

    # Ask the user for an option in the terminal
    choice = Prompt.ask(
        "\nSelect an option",
        choices=["1", "2", "3", "lang", "api", "git", "q"],
        default="q",
    ).lower()

    if choice in ["1", "lang"]:
        show_language_help()
    elif choice in ["2", "api"]:
        show_api_help()
    elif choice in ["3", "git"]:
        show_git_tutorial()
    else:
        console.print(f"[yellow]Exiting help...[/yellow]")

    raise typer.Exit()


if __name__ == "__main__":
    app()
