'''
devoriales.com, 2023
Path: json/get_data_from_files.py
description: get data from files
'''

import json


# get data from a file in data folder
with open('data/cars') as f:  # open the file in read mode
    data = json.load(f)  # type dict

# print the data
# print(data)

# print the manufacturer of all the cars
for car in data['cars']:
    print(car['manufacturer'], end=': ')
    print(car['model'])
    
