import rich_helpers as r
import load as l
import search as s
from rich.prompt import Prompt
r.title()
r.description()
option = r.choose_option()
input_text = r.imput_text()
MARVEL = l.load_csv()
search = s.search(MARVEL, 0, input_text)
r.table_maker(search)
print(search[0])
