from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_language_help():
    url = "https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"
    table = Table(title="Example of supported Language Shortcuts")
    table.add_column("Shortcut", style="cyan")
    table.add_column("Language", style="magenta")
    common = {
        "en": "English",
        "pt": "Portuguese",
        "es": "Spanish",
        "zh": "Chinese",
        "ja": "Japanese",
        "ru": "Russian",
        "de": "German",
        "ko": "Korean",
        "fr": "French",
        "it": "Italian"
    }
    for code, lang in common.items():
        table.add_row(code, lang)
    console.print(table)
    console.print(f"Visit: {url} to check all language codes available\n")
    console.print(
        f"To generate commit messages in a specific language, run: [italic]python main.py 'language_code'[/italic] (e.g., [italic]python main.py pt[/italic] for Portuguese). If no language is specified, English will be used by default.\n"
    )


def show_api_help():
    text = """
1. Visit: [blue underline]https://aistudio.google.com[/blue underline] to get started.
2. Generate a [bold]Gemini API Key[/bold] (make sure it's active and you have enough tokens/requests).
3. Create a file named [bold].env[/bold] in the project root.
4. Add this line to the file: [green]GEMINI_API_KEY = "your key here"[/green]
5. Save the file and run this tool: [italic]python main.py[/italic] for English default or select a language using [italic]python main.py 'language_code'[/italic] (e.g., [italic]python main.py pt[/italic] for Portuguese).
    """
    console.print(Panel(text, title="API Setup", expand=False))


def show_git_tutorial():
    url = "https://git-scm.com/cheat-sheet"
    text = """
[bold yellow]Step 1:[/bold yellow] Make sure you are in a git repo: [italic]git init[/italic]
[bold yellow]Step 2:[/bold yellow] Stage your changes: [italic]git add .[/italic]
[bold yellow]Step 3:[/bold yellow] Run this tool: [italic]python main.py[/italic] for English default or [italic]python main.py 'language_code'[/italic] (e.g., [italic]python main.py pt[/italic] for Portuguese) for typed language.
    """
    console.print(Panel(text, title="Git Basics", expand=False))
    console.print(
        f"For further information, visit: {url} to check basic Git commands and full documentation. \n"
    )
