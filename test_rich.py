import rich_helpers as r
import load as l
import search as s
from rich.prompt import Prompt
r.title()
r.description()
option = r.choose_option()
input_text = r.imput_text()
MARVEL = l.load_csv()
result = s.search(MARVEL, 0, input_text)
result_temp = []
for idx, row in enumerate(result):
    if idx % 10 == 0 and idx != 0:
        print_table = Prompt.ask('[1] Print 10 row table, [2] Exit', choices=["1", "2"], show_choices=False)
        if print_table == "1":
            print(len(result_temp))
            r.table_maker(result_temp, input_text)
            result_temp = []
        else:
            result_temp = []
            break
    result_temp.append(row)
