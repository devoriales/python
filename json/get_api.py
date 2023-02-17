'''
devoriales.com, 2023
Path: json/get_data_from_files.py
description: get data from api request using requests library
'''

import requests
import json

# get fake api data from dummyJSON API
# https://dummyapi.io/data/api/user?limit=10

# get the data
response = requests.get("https://dummyjson.com/products")
# print(response)  # <Response [200]>

# print different parts of the response
# print(response.status_code)  # 200
# print(response.headers)  # prints out the headers
# print(response.text)  # prints out the text of the response (json data)
# print(response.content)  # prints out the content of the response (json data)


# deserialize the data
data = response.json()  # type dict

#
# get all the titles of the products via list comprehension
titles = [product['title'] for product in data['products']
          if product['title'].startswith('iPhone')]
print(titles)


# get information about products in titles
for title in titles:  # loop through the titles
    # print title and price on the same line
    # end='' prevents the print function from adding a new line
    print(title, end=': ')
    # print the price
    print([product['price'] for product in data['products']  # list comprehension to get the price
           if product['title'] == title][0])
