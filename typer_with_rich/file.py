import typer

def main(name: str, lastname: str, age: int,  formal: bool = False):
    if formal:
        print(f"Good day, Ms. {name} {lastname}. You are {age} years old.")
    else:
        print(f"Hello, {name} {lastname}! You are {age} years old.")
        
if __name__ == "__main__":
    typer.run(main)
