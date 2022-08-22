from rich.console import Console
from rich.panel import Panel


def title():
    title = Panel('MARVEL COMICS DATASET')
    console = Console()    
    console.print(title, style="italic bright_red", justify='center')
