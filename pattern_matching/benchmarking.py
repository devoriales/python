# devoriales.com, 2022
# Path: pattern_matching/benchmarking.py
# description: benchmarking switch case vs if else in python

import time

# create a list of names
my_name_list = []

# context manager to open the file and read the names and append them to the list
with open ('data', 'r') as f:
    for line in f:
        my_name_list.append(line)
        
# add a name to the list to the very end
my_name_list.append('Moby Dick')


# check if name is in list with switch case
def check_common_name(name):
    # switch case 
    for x in my_name_list:
        match name:
            case str(x):
                return True
            case _:
                return False

# check if name is in list with if else
def check_with_if(name):
    # if else
    for x in range(len(my_name_list)): 
        if name == my_name_list[x].splitlines()[0]:
            return True
    return False

# time the functions
start_if = time.time() # time the function with if else
print(check_with_if('Moby Dick'))
end_if = time.time()
print(end_if - start_if)
result_if = end_if - start_if # get the result of the function with if else


start_switch = time.time() # time the function with switch case
print(check_common_name('Moby Dick'))
end_switch = time.time()
print(end_switch - start_switch)
result_switch = end_switch - start_switch # get the result of the function with switch case

#compare the results
if result_if > result_switch:
    print('switch case is faster')
else:
    print('if else is faster')


