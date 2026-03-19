import subprocess
import typer


def get_git_diff():
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    return result.stdout


def apply_commit(message):
    if typer.confirm("Do you wish to apply this commit?"):
        result = subprocess.run(["git", "commit", "-m", message])
        return result.returncode == 0  # Returns True if success
    return False
