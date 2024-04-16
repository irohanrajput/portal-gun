import typer
from rich import print

app = typer.Typer()

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
    typer.echo("Shooting portal gun")
@app.command()    
def load():
    '''
    load the portal gun 
    '''
    typer.echo(print("[blink red on black]loading the fuckin portal gun "))