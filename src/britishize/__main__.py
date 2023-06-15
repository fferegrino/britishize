import typer
from britishize.britishize import britishize

app = typer.Typer()


@app.command()
def to_british(text: str):
    britishized = britishize(text)
    print(britishized)


def main():
    app()


if __name__ == "__main__":
    main()
