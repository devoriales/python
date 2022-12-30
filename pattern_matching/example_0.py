'''
devoriales.com
Path: pattern_matching/example_0.py
description: type based dispatch using if else and match case
'''


# # type based dispatch using if else
# def check_type(x):
#     if type(x) == int:
#         return f"{x} is an integer"
#     elif type(x) == float:
#         return f"{x} is a float"
#     elif type(x) == list:
#         return f"{x} is a list"
#     elif type(x) == tuple:
#         return f"{x} is a tuple"
#     elif type(x) == dict:
#         return f"{x} is a dict"
#     elif type(x) == str:
#         return f"{x} is a string"
#     else:
#         return f"{x} is a type that I don't know about"


# type based using structural pattern matching
def check_type(x):
    print('match statement is working')
    match x:
        case int():
            return f"{x} is an integer"
        case float():
            return f"{x} is a float"
        case list():
            return f"{x} is a list"
        case tuple():
            return f"{x} is a tuple"
        case dict():
            return f"{x} is a dict"
        case str():
            return f"{x} is a string"
        case _:
            return f"{x} is a type that I don't know about"


print(check_type(1))    # 1 is an integer
print(check_type(1.0))  # 1.0 is a float
print(check_type([]))   # [] is a list
print(check_type(()))   # () is a tuple
print(check_type({}))   # {} is a dict
print(check_type(''))   #  is a string
