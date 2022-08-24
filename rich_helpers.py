from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from rich import box


def title():
    title = Panel('MARVEL COMICS DATASET')
    console = Console()
    console.print(title, style="italic bright_red", justify='center')


def description():
    description = Text("\nThe dataset contains info on all the comic books ever released in the Marvel Universe. You can search for your favorite writer, your favorite series or the comics that came out during your childhood.\n")
    description.stylize("bold magenta")
    console = Console()
    console.print(description)


def choose_option():
    option = Prompt.ask('[1] Search for a writer, [2] Search for a series, [3] Search for a comic book, [4] Search for a Year of activity, [5] Exit', choices=[
                        "1", "2", "3", "4", "5"], show_choices=False)
    return option

def imput_text():
    text = Prompt.ask('Enter your search')
    return text

def table_maker(data):
    table = Table(title="Marvel", show_header=True,
                  header_style="bold magenta", box=box.DOUBLE_EDGE, show_lines=True)
    for col in data[0]._fields:
        table.add_column(col.replace("_", " ").title())

    for row in data:
        table.add_row(*row)

    console = Console()
    console.print(table)
