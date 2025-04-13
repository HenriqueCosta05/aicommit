import subprocess
from typing import Optional

def get_git_diff(staged_only: bool = True) -> Optional[str]:
    """Get git diff of changes."""
    try:
        cmd = ["git", "diff", "--cached"] if staged_only else ["git", "diff"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout if result.stdout.strip() else None
    except subprocess.CalledProcessError:
        return None

def commit_changes(message: str) -> bool:
    """Commit changes with the given message."""
    try:
        subprocess.run(["git", "commit", "-m", message], check=True)
        return True
    except subprocess.CalledProcessError:
        return False