import re
from rich.prompt import Prompt

def search(data, option, text):
    result = []
    text_complete = auto_complete(data, option, text)
    for row in data:
        if row[option] == text_complete:
            result.append(row)
    return result

def auto_complete(data, option, text):
    complete = ""
    mem = None
    for row in data:
        if mem != row[option]:
            mem = row[option]    
            if row[option].startswith(text.title()):
                confirm = Prompt.ask("Did you mean {}?".format(row[option]), choices=["y", "n"])
                if confirm == "y":
                    complete = row[option]
                    break
                else:
                    continue
    return complete        