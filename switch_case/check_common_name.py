
# Devoriales.com, 2022
# Path: switch_case/check_common_name.py
# Description: Checking if a name is common or not using switch case and match statement

# # checks if a name is common or not. Uses if else statements
# def check_common_name(name):
#     # switch case 
#     if name == 'John':
#         return True
#     elif name == 'Mary':
#         return True
#     elif name == 'James':
#         return True
#     elif name == 'Sarah':
#         return True
#     elif name == 'Robert':
#         return True
#     else:
#         return False

# checks if a name is common or not. Uses match statement 


def check_common_name(name):
    # switch case 
    match name:
        case 'John':
            return True
        case 'Mary':
            return True
        case 'James':
            return True
        case 'Sarah':
            return True
        case 'Robert':
            return True
        case _: # default case which is the same as else
            return False
    

print(check_common_name('John'))  # checks if a name is common or not
print(check_common_name('Aleks'))  # checks if a name is common or not
