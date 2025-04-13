import os
import click
from .git_utils import get_git_diff, commit_changes
from .ai_handler import AICommitMessageGenerator

@click.group()
def cli():
    """AI-powered git commit message generator."""
    pass

@cli.command(name="generate")
@click.option("--staged-only", is_flag=True, default=True, 
              help="Only consider staged changes")
@click.option("--auto-commit", is_flag=True, default=False,
              help="Automatically commit with the generated message")
@click.option("--model", default=None,
              help="AI model to use for generation")
def generate(staged_only: bool, auto_commit: bool, model: str):
    """Generate commit messages using AI."""
    ai = AICommitMessageGenerator(model=model)
    
    # Initialize the AI handler
    click.echo("Initializing AI commit message generator...")
    ai.initialize()
    
    diff = get_git_diff(staged_only)
    if not diff:
        click.echo("No changes detected. Use --no-staged-only for all changes.")
        return
    
    click.echo("Generating commit message...")
    message = ai.generate_commit_message(diff)
    
    click.echo("\nSuggested commit message:")
    click.echo(click.style(message, fg="green"))
    
    if auto_commit:
        if commit_changes(message):
            click.echo("Changes committed successfully!")
        else:
            click.echo("Failed to commit changes.", err=True)
    else:
        if click.confirm("Would you like to commit with this message?"):
            if commit_changes(message):
                click.echo("Changes committed successfully!")
            else:
                click.echo("Failed to commit changes.", err=True)

# This is important! Update your main function to use the new CLI group
def main():
    """Entry point for the CLI."""
    cli()

if __name__ == "__main__":
    main()