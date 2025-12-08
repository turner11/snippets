#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10,<3.11"
# dependencies = [
#   "rich",
#   "rich-click>=1.9.4",
# ]
# ///

import click
import rich_click as rc

# --- 1. CONFIGURE RICH-CLICK ---
# Set the base style for rich_click (optional, but good for consistency)
rc.rich_click.USE_MARKDOWN = True
rc.rich_click.SHOW_ARGUMENTS = True
rc.rich_click.GROUP_COMMANDS_WITH_HEADING = True
rc.rich_click.COMMAND_GROUPS = {
    "my_cli": [
        {
            "name": "Main Commands",
            "commands": ["process", "status"],
        },
        {
            "name": "Management",
            "commands": ["config"],
        },
    ],
    # You can define groups for subcommands too (e.g., for 'process')
    # "process": [ ... ]
}
# Optionally define custom styles for things like options/arguments/usage
# rc.rich_click.STYLE_OPTION = "bold green"
# rc.rich_click.STYLE_ARGUMENT = "bold yellow"


# --- 2. MAIN GROUP COMMAND ---

# Use the decorated @rc.group instead of @click.group
@rc.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """
    ✨ **My Awesome CLI Tool**

    A powerful command-line interface demonstrating
    the beautiful output of `rich-click`.

    Use the `--help` option on any command for more details.
    """
    pass

# --- 3. SUBCOMMAND 1: PROCESS (with Options and Arguments) ---

@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(),
    default="output",
    show_default=True,
    help="The directory where processed results will be saved.",
)
@click.option(
    "--fast-mode",
    is_flag=True,
    default=False,
    help="Enables a quicker, but less detailed processing routine.",
)
def process(input_file, output_dir, fast_mode):
    """
    Process a specific **INPUT_FILE**.

    This command handles the core logic of the application.
    It takes an input file and generates results in the specified
    output directory.
    """
    rc.rich_click.console.print(
        f"[bold blue]Processing:[/bold blue] {input_file}"
    )
    rc.rich_click.console.print(
        f"  [cyan]Output Directory:[/cyan] {output_dir}"
    )
    if fast_mode:
        rc.rich_click.console.print(
            "[yellow]  Fast Mode is ENABLED. Results may vary.[/yellow]"
        )
    # Your processing logic goes here...
    rc.rich_click.console.print(
        "\n[bold green]✅ Processing complete![/bold green]"
    )

# --- 4. SUBCOMMAND 2: STATUS (Simple Command) ---

@cli.command()
def status():
    """
    Show the **current status** of the tool.

    Provides a quick overview of recent activity and configuration.
    """
    rc.rich_click.console.print(
        "Checking system status..."
    )
    # Your status checking logic goes here...
    rc.rich_click.console.print(
        "[bold green]System is operational.[/bold green]"
    )
    
# --- 5. SUBCOMMAND 3: CONFIG (Management Command) ---

@cli.command()
def config():
    """
    Manage the **application configuration**.

    Allows viewing and editing of persistent settings.
    """
    rc.rich_click.console.print(
        "Opening configuration editor..."
    )
    # Your configuration logic goes here...
    rc.rich_click.console.print(
        "[bold magenta]Configuration loaded.[/bold magenta]"
    )


# --- 6. EXECUTION BLOCK ---

if __name__ == "__main__":
    cli()
