# Python Data Processing App

## Introduction

This project is a python data processing application built with python 3.10 which includes getting data from CSV, converting it into json and then filtering, sorting aggregating and transforming processes are demonstrated through the imported data.
The libraries used in the projects are pandas for data processing, json for using json data and matplotlib for visualization.

The main feature for the tasks taken for the data processing of weather data is max temperature here.

So, for filtering and sorting, max temperature is taken into account.

Also, for aggregation, average value is calculated.

For transformation, it is simply demonstrated by calculating fahrenheit value of celsius value in max temperature.

## Installation and Usage

1. Cloning the project
```
   git clone https://github.com/jharahul968/python-task.git

   cd python-task
```
2. Virtual Environment Setup
```
   pip install virtualenv

   python -m venv venv

   source venv/bin/activate (for linux)
```
3. Running the script
```
   python weather_json.py
```
4. You will be prompted to enter a value only after which the maximum temperature will be filtered.

    Type the value and press enter.

    The final results will be saved in /results/ directory and a time series graph will also show the series of 
maximum temperature over time.

Additional scripts

4. Testing the code
```
    python tests.py
```