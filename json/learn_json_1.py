'''
devoriales.com
Path: json/learn_json_1.py
description: json

JSON stands for JavaScript Object Notation

'''


import json

# JSON data as a string
json_data = '{"manufacturer": "Ferrari", "model": "LaFerrari", "year": 2013, "engine": {"type": "hybrid", "displacement": 6.3}, "topSpeed": 217, "acceleration": {"zeroToSixty": 2.4, "zeroToTwoHundred": 15}, "colors": ["rosso corsa", "yellow", "black"], "isLimitedEdition": true}'

# Load the JSON data into a Python object
car_data = json.loads(json_data)

# print individual values
print(car_data["manufacturer"])
print(car_data["model"])
print(car_data["acceleration"]["zeroToSixty"])
