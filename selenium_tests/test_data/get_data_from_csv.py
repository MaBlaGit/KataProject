import csv


def get_data(file_name):
    rows = list()
    csv_file_opener = open(file_name, 'r')
    reader = csv.reader(csv_file_opener)
    # skip header of the csv file
    next(reader)
    for data in reader:
        rows.append([data[0]])
    return rows
