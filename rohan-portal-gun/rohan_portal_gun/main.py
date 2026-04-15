import time
import random

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
from rich.text import Text

app = typer.Typer()
console = Console()


@app.callback()
def callback():
    '''
    Awesome portal gun
    '''


@app.command()
def shoot():
    '''
    shoot the portal gun
    '''
    with Progress(
        SpinnerColumn(style="bold green"),
        TextColumn("[bold green]Charging portal gun..."),
        BarColumn(complete_style="green", finished_style="bright_green"),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("charge", total=30)
        for _ in range(30):
            time.sleep(0.04)
            progress.advance(task)

    frames = [
        "[green]        .        [/green]",
        "[green]      . o .      [/green]",
        "[bright_green]    . o O o .    [/bright_green]",
        "[bright_green]  . o O @ O o .  [/bright_green]",
        "[yellow]. o O @ * @ O o .[/yellow]",
        "[bright_yellow]o O @ * ~ * @ O o[/bright_yellow]",
        "[bright_white]O @ * ~ ! ~ * @ O[/bright_white]",
    ]
    with Live(console=console, refresh_per_second=20, transient=True) as live:
        for frame in frames:
            live.update(Align.center(Text.from_markup(frame)))
            time.sleep(0.08)

    console.print(Panel.fit(
        "[bold bright_green]>>> PORTAL OPENED <<<[/bold bright_green]\n[dim]wubba lubba dub dub![/dim]",
        border_style="bright_green",
    ))


@app.command()
def load():
    '''
    load the portal gun
    '''
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold red"),
        TextColumn("[bold red]Loading the fuckin portal gun[/bold red]"),
        BarColumn(complete_style="red", finished_style="bright_red"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        transient=True,
    ) as progress:
        task = progress.add_task("load", total=50)
        for _ in range(50):
            time.sleep(0.03)
            progress.advance(task)

    console.print("[blink bold red on black] ⚡ PORTAL GUN LOADED ⚡ [/blink bold red on black]")


@app.command()
def sleep():
    '''
    go back to sleep
    '''
    zzz_frames = ["z  ", "zZ ", "zZz", "Zz ", "z  "]
    with Live(console=console, refresh_per_second=6, transient=True) as live:
        for _ in range(12):
            frame = random.choice(zzz_frames)
            live.update(Text.from_markup(f"[bold magenta]😴 {frame}[/bold magenta]"))
            time.sleep(0.15)

    console.print(Panel.fit(
        "[red blink]okay I am going to sleep now, Good Day Sir.[/red blink]",
        border_style="magenta",
    ))
