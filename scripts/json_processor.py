import json


def json_reader(file_location):
    with open(file_location) as f:
        return json.load(f)
