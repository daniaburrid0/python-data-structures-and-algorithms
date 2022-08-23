from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def title():
    title = Panel('MARVEL COMICS DATASET')
    console = Console()
    console.print(title, style="italic bright_red", justify='center')

def description():
    description = Text("\nThe dataset contains info on all the comic books ever released in the Marvel Universe. You can search for your favorite writer, your favorite series or the comics that came out during your childhood.\n")
    description.stylize("bold magenta")
    console = Console()
    console.print(description)