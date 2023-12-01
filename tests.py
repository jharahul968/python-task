import unittest
import os
import pandas as pd
import json
from weather_json import csv_to_json, filter_data, sort_data, aggregate_data, transform_data, save_json


class TestWeatherJsonFunctions(unittest.TestCase):
    CSV_PATH = 'resources/test_data.csv'
    JSON_PATH = 'resources/test_data.json'
    RESULT_PATH = 'results/test_result.json'

    def setUp(self):
        data = {
            'MaxTemp': [25.2, 27, 12.2, 30.9],
        }
        df = pd.DataFrame(data)
        df.to_csv(self.CSV_PATH, index=False)

    def tearDown(self):
        if os.path.exists(self.CSV_PATH):
            os.remove(self.CSV_PATH)
        if os.path.exists(self.JSON_PATH):
            os.remove(self.JSON_PATH)
        if os.path.exists(self.RESULT_PATH):
            os.remove(self.RESULT_PATH)

    def test_csv_to_json(self):
        # Test CSV to JSON conversion
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        self.assertIsInstance(temp_data, list)
        self.assertEqual(len(temp_data), 4)

    def test_filter_data(self):
        # Test data filtering
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        filtered_data = filter_data(temp_data, lambda x: x.get('MaxTemp') > 25)
        self.assertIsInstance(filtered_data, list)
        self.assertEqual(len(filtered_data), 3)

    def test_sort_data(self):
        # Test data sorting
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        sorted_data = sort_data(temp_data, 'MaxTemp')
        self.assertIsInstance(sorted_data, list)
        self.assertEqual(len(sorted_data), 4)
        self.assertEqual(sorted_data[0]['MaxTemp'], 12.2)

    def test_aggregate_data(self):
        # Test data aggregation
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        aggregated_result = aggregate_data(temp_data, 'MaxTemp', sum)
        self.assertIsInstance(aggregated_result, float)
        self.assertEqual(aggregated_result, sum([25.2, 27, 12.2, 30.9]))

    def test_transform_data(self):
        # Test data transformation
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        transform_data(temp_data, 'MaxTemp', lambda x: x *
                       2, 'TransformedMaxTemp')
        transformed_values = [x['TransformedMaxTemp'] for x in temp_data]
        self.assertEqual(transformed_values, [50.4, 54, 24.4, 61.8])

    def test_save_json(self):
        # Test saving JSON data to a file
        temp_data = csv_to_json(self.CSV_PATH, self.JSON_PATH)
        save_json(temp_data, self.RESULT_PATH)
        self.assertTrue(os.path.exists(self.RESULT_PATH))

        with open(self.RESULT_PATH, 'r', encoding='UTF-8') as file:
            saved_data = json.load(file)

        self.assertIsInstance(saved_data, list)
        self.assertEqual(len(saved_data), 4)


if __name__ == '__main__':
    unittest.main()
