'''
devoriales.com, 2022
Path: pattern_matching/data_deconstruction.py
description: data deconstruction - tuple unpacking
'''

# data deconstruction with if else
def data_deconstruction(x):
    if type(x) == tuple:
        return f"{x[0]} is working as a {x[1]} at {x[2]}"
    else:
        return f"{x} is not a tuple"

print(data_deconstruction(('Oliver', 'developer', 'Google')))

# data deconstruction with match case
def data_deconstruction(x):
    match x:
        case (name, job, company):
            return f"{name} is working as a {job} at {company}"
        case _:
            return f"{x} is not a tuple"

print(data_deconstruction(('Sanja', 'designer', 'Apple')))

my_tuple = ('Woman', 'singing')
obj, verb = my_tuple
print(obj) # 'woman'
print(verb)  # 'singing'
