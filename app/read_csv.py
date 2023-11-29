import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        return data
