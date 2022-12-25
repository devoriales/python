# devoriales.com, 2022
# Path: switch_case/switch_case_with_AND_condition.py
# description: benchmarking switch case vs if else in python
# tags: python, switch case with AND condition


# with AND condition
def sportcars(*car):
    print(car)
    # switch case 
    match car:
        case 'Ferrari', 'Lamborghini': # multiple cases with AND condition
            return 'Sportscars'
        case _:
            return 'Not sportscars'

# if else
# def sportcars(*car):
#     car1, car2 = car
#     print(type(car))
#     if car1 == 'Ferrari' and car2 == 'Lamborghini':
#         return 'Sportscars'
#     else:
#         return 'Not a sportscar'

print(sportcars('Ferrari', 'Lamborghini'))  # multiple cases with AND condition will return Sportscars
print(sportcars('Fiat', 'Lamborghini'))  # multiple cases with AND condition will return Not a sportscar

