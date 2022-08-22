import csv
from collections import namedtuple


def load_csv():
    """Load Marvel CSV data into a list of namedtuples."""
    csv_file = 'csv/Marvel_Comics.csv'
    marvel_data = None
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        Marvel = namedtuple('Marvel', reader.fieldnames)
        marvel_data = [Marvel(**row) for row in reader]
        file.close()
    return marvel_data
