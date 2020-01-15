import csv
import json


def csv_reader(file_location):
    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        for row in data:
            try:
                row['Lat'] = float(row['Lat'])
                row['Long'] = float(row['Long'])
                row['Altitude'] = float(row['Altitude'])
            except Exception as exp:
                raise ValueError('Invalid input: ' + str(exp))

        return data


def json_reader(file_location):
    with open(file_location) as f:
        return json.load(f)
