import rich_helpers as r
import load as l
r.title()
r.description()
option = r.choose_option()
MARVEL = l.load_csv()
print(option)
r.table_maker([MARVEL[100],MARVEL[101], MARVEL[102]], "Comic Name")