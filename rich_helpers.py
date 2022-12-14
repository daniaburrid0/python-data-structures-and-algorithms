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
    description = Text("\nThe dataset contains info on all the comic books ever released in the Marvel Universe. You can search for your favorite writer, your favorite series or the comics that came out during your childhood and more.\n")
    description.stylize("bold magenta")
    console = Console()
    console.print(description)


def choose_option():
    option = Prompt.ask('[1] Search for a Comic Name, [2] Search for a Issue Title, [3] Search for a Writer, [4] Search for a Penciler, [5] Exit', choices=[
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


def bye():
    bye = Text("\nThank you for using this program.\n")
    bye.stylize("bold magenta")
    console = Console()
    console.print(bye)


def no_result():
    no_result = Text("\nNo result found.\n")
    no_result.stylize("bold magenta")
    console = Console()
    console.print(no_result)


def bigger_than_10():
    bigger = Text("\nPrinting 10 results.\n")
    bigger.stylize("bold magenta")
    console = Console()
    console.print(bigger)


def continue_printing():
    con = Prompt.ask("Do you want to print more results?", choices=["y", "n"])
    return con


def last_result():
    last = Text("\nPrinting last result.\n")
    last.stylize("bold magenta")
    console = Console()
    console.print(last)
