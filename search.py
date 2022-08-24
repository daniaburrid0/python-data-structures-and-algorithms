import re

def search(marvel, option, text):
    result = []
    for row in marvel:
        if re.search(text, row[option], re.IGNORECASE):
            result.append(row)
    return result