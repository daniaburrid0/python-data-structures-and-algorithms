from rich.console import Console
from rich.markdown import Markdown


def title():
    title = '# Marvel Comic Books Dataset'
    console = Console()
    md = Markdown(title)
    console.print(md)

def description():
    description = '## The dataset contains info on all the comic books ever released in the Marvel Universe.'
    console = Console()
    md = Markdown(description)
    console.print(md)

title()
description()
