import typer
from rich import print

data = {
    "name": "John",
    "lastname": "Doe",
    "formal": False,
    "item": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

def main():
    print("[bold white on red blink]this is the data")
    print (data)
    
    
if __name__ == "__main__":
    typer.run(main)