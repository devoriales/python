'''
devoriales.com, 2022
Path: pattern_matching/example_8.py
description: data deconstruction with match case
'''

# determine action like obj and verb
def determine_action(x):
    match x:
        case (obj, verb): # data deconstruction
            return f"{obj} is {verb} becase it is type {type(x)}" 
        case _: # default case
            return f"{x} is not a tuple becase it is type {type(x)}"


print(determine_action(('dog', 'barking')))
print(determine_action(('cat', 'meowing')))
# not a tuple
print(determine_action('dog'))

