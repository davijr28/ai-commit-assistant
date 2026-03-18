from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def show_language_help():
    table = Table(title="Example of supported Languages Shortcuts")
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
    console.print("Visit: [link=https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes][bold cyan]ISO 639-1 Codes List[/bold cyan][/link] to check all language codes available\n")


def show_api_help():
    text = """
1. Go to [bold blue]Google AI Studio[/bold blue].
2. Generate a [bold]Gemini API Key[/bold].
3. Create a file named [bold].env[/bold] in the project root.
4. Add this line: [green]GEMINI_API_KEY = "your_key_here"[/green]
    """
    console.print(Panel(text, title="API Setup", expand=False))


def show_git_tutorial():
    text = """
[bold yellow]Step 1:[/bold yellow] Ensure you are in a git repo: [italic]git init[/italic]
[bold yellow]Step 2:[/bold yellow] Stage your changes: [italic]git add .[/italic]
[bold yellow]Step 3:[/bold yellow] Run this tool: [italic]python main.py[/italic] for English default or [italic]python main.py 'language'[/italic] (e.g. pt, for Portuguese) for typed language.
    """
    console.print(Panel(text, title="Git Basics", expand=False))
