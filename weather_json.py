"""
Python-based Data Processing Tool

This script defines functions for data processing in python.

Author: Rahul Kumar Jha
Date: 1 December, 2023
"""

import json
import pandas as pd


# Function to convert CSV to JSON
def csv_to_json(csv_path, json_path):
    """
    Convert a CSV file to JSON format.

    Parameters:
    - csv_path (str): Path to the input CSV file.
    - json_path (str): Path to save the output JSON file.

    Returns:
    - list: List of dictionaries representing the JSON data.
    """
    try:
        print(f"Getting csv data from location {csv_path}..")
        df = pd.read_csv(csv_path)
        print(f"Saving json data at location {json_path}..")
        df.to_json(json_path, orient='records', indent=2)
        print("Opening json file in program..")
        with open(json_path, 'r', encoding='UTF-8') as file:
            file = json.load(file)

        return file
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading the file: {e}")
        return None


# Function to filter data based on a condition
def filter_data(data, condition):
    """
    Filter data based on a given condition.

    Parameters:
    - data (list): List of dictionaries representing the data.
    - condition (function): A lambda function defining the filtering condition.

    Returns:
    - list: List of filtered dictionaries.
    """
    try:
        return [x for x in data if condition(x)]
    except KeyError as e:
        print(f"Error filtering the data: {e}")
        return None


# Function to sort data based on a key
def sort_data(data, key):
    """
    Sort data based on a given key.

    Parameters:
    - data (list): List of dictionaries representing the data.
    - key (str): Key based on which the data should be sorted.

    Returns:
    - list: List of sorted dictionaries.
    """
    try:
        return sorted(data, key=lambda x: x[key])
    except (TypeError, KeyError) as e:
        print(f"Error sorting data: {e}")
        return None


# Function to aggregate data using a specified function
def aggregate_data(data, feature, aggregating_function):
    """
    Aggregate data using a specified function.

    Parameters:
    - data (list): List of dictionaries representing the data.
    - feature (str): Feature on which aggregation is performed.
    - aggregating_function (function): Aggregating function to be applied.

    Returns:
    - float: Aggregated result.
    """
    try:
        return aggregating_function(x[feature] for x in data)
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error aggregating data: {e}")
        return None


# Function to transform data based on a given function
def transform_data(data, feature, transforming_function, transformed_data):
    """
    Transform data based on a given function.

    Parameters:
    - data (list): List of dictionaries representing the data.
    - feature (str): Feature to be transformed.
    - transforming_function (function): Transformation function to be applied.
    - transformed_data (str): Key to store the transformed data.
    """
    try:
        for i in data:
            i[transformed_data] = transforming_function(i[feature])
    except TypeError as e:
        print(f"Error transforming data: {e}")


# Function to save JSON data to a file
def save_json(data, result_path):
    """
    Save JSON data to a specified file.

    Parameters:
    - data (list): List of dictionaries representing the data.
    - result_path (str): Path to save the JSON result.
    """
    with open(result_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print(f"The saved data is in location {result_path}.")


if __name__ == '__main__':
    CSV_PATH = 'resources/weather.csv'
    JSON_PATH = 'resources/weather.json'
    RESULT_PATH = 'results/result.json'
    # Convert CSV to JSON
    temp_data = csv_to_json(csv_path=CSV_PATH, json_path=JSON_PATH)
    # Filter data where MaxTemp is greater than 25
    temp_gt_25 = filter_data(temp_data, lambda x: x.get('MaxTemp') > 25)
    # Sort filtered data based on MaxTemp
    temp_sorted = sort_data(temp_gt_25, 'MaxTemp')
    # Calculate average MaxTemp
    average_temp = aggregate_data(
        temp_sorted, 'MaxTemp', sum) / len(temp_sorted)
    print(f"The average max temp is: {average_temp}")
    # Transform MaxTemp to Fahrenheit and save the result
    transform_data(
        temp_sorted,
        'MaxTemp',
        transforming_function=lambda x: x * 9/5 + 32,
        transformed_data='MaxTempFahrenheit')
    save_json(temp_sorted, result_path=RESULT_PATH)
