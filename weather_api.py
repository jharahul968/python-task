import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.environ["API_KEY"]
latitude_ktm = 27.7172
longitude_ktm = 85.3240
days = 5

response = requests.get(f'''
    https://pro.openweathermap.org/data/2.5/forecast/climate
    ?lat={latitude_ktm}&lon={longitude_ktm}&appid={API_KEY}&cnt={days}''')
response = response.json()

print(response)
