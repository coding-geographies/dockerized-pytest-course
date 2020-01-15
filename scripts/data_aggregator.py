import csv
import json
from statistics import mean, median


def count_electric_scooter_usage(data):
    # total count = len([x for x in data if x['electric_scooter'] == True])
    electric_scooter_data  = [x for x in data if x['electric_scooter'] == True]

    usage_dictionary = {
            'Daily': 0,
            'Monthly': 0,
            'Never': 0,
            'Often': 0,
            'Once': 0,
            'Seldom': 0,
            'UNKNOWN': 0,
            'Weekly': 0,
            'Yearly': 0,
    }
    for scooter in electric_scooter_data:
        if scooter['usage'] in usage_dictionary:
            usage_dictionary[scooter['usage']] += 1
        else:
            usage_dictionary['UNKNOWN'] += 1

    total_electric_scooters = sum(usage_dictionary.values())
    return total_electric_scooters, usage_dictionary


def get_altitudes_per_country(data, country):
    return [x['Altitude'] for x in data if x['Country'] == country]


def atitude_stat_per_country(data, country, stat):
    country_altitude_list = []
    for row in data:
        if row['Country'] == country:
            country_altitude_list.append(row['Altitude'])
    if stat.lower() == 'mean':
        result = mean(country_altitude_list)
    elif stat.lower() == 'median':
        result = median(country_altitude_list)
    return {'Country': country,
            stat: round(result, 2)
    }


def csv_writer(row_data, output_location):
    fieldnames = row_data.keys()
    writer = csv.DictWriter(output_location, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row_data)
    # return csv.readlines()
