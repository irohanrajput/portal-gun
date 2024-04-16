import typer
def main(name: str, lastname: str = "", formal: bool = False):
    
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    
    if formal:
        print(f"Good day, Ms. {name} {lastname}.")
    else:
        print(f"Hello, {name} {lastname}!")
        
if __name__ == "__main__":
    typer.run(main)
    
    
    
# A CLI option with a value like --lastname (contrary to a CLI option without a value, a bool flag, like --formal or --size) takes as its value whatever is at the right side of the CLI option.