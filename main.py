import typer
from rich.console import Console
from help import show_language_help, show_api_help, show_git_tutorial
from git_utils import get_git_diff, apply_commit
from llm import generate_commit
from typing import Optional
import pycountry

app = typer.Typer(help="AI Commit Message Generator")
console = Console()


def validate_lang(value: str):
    query = value.strip().lower()
    language = pycountry.languages.get(alpha_2=query) or pycountry.languages.get(
        name=query.capitalize()
    )
    if language and hasattr(language, "alpha_2"):
        return language.name
    return None


# This is what runs when you just type 'python main.py' or 'python main.py pt'
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    language: Optional[str] = typer.Argument(
        None, help="Language code (e.g., 'pt'). Leave blank for English."
    ),
):
    # Check if subcommand is typed
    if ctx.invoked_subcommand is not None:
        return

    # If no subcommand, but language is None, default to English
    if language is None:
        language = "en"

    # Validate the language
    target_lang = validate_lang(language)
    if not target_lang:
        console.print(
            f"[yellow]Warning:[/yellow] '{language}' not recognized. Please, check [italic]python main.py help[/italic] to know more."
        )
        raise typer.Exit()

    # Check staged changes
    diff = get_git_diff()
    if not diff.strip():
        console.print(
            "[bold red]No staged changes found. Please, check [italic]python main.py help[/italic] to know more.[/bold red]"
        )
        raise typer.Exit()

    with console.status(f"[bold green]Generating {target_lang} commit..."):
        message = generate_commit(diff, target_lang)

    console.print(f"\n[bold]Suggested ({target_lang}):[/bold] [green]{message}[/green]")

    if apply_commit(message):
        console.print("[bold blue]✓ Committed successfully![/bold blue]")


# --- Help Subcommands ---


@app.command(name="help")
def help_menu():
    """Show instructions for Languages, API, or Git."""
    console.print("\n[bold cyan]Available Help Topics:[/bold cyan]")
    console.print("1. [bold]lang[/bold] - Supported languages")
    console.print("2. [bold]api[/bold] - How to setup your .env key")
    console.print("3. [bold]git[/bold] - Quick Git tutorial")
    console.print("\nUsage: [italic]python main.py help [topic][/italic]")


@app.command()
def lang():
    # List supported language shortcuts
    show_language_help()


@app.command()
def api():
    # How to configure the Gemini API key
    show_api_help()


@app.command()
def git():
    # Git basics for this tool
    show_git_tutorial()


if __name__ == "__main__":
    app()
