# devoriales.com, 2022
# Path: switch_case/switch_case_with_OR_condition.py
# description: benchmarking switch case vs if else in python
# tags: python, switch case with OR condition


# with OR condition
def sportcars(car):
    print(car)
    # switch case 
    match car:
        case 'Ferrari' | 'Lamborghini' | 'Porsche' | 'Aston Martin': # multiple cases with OR condition
            return 'Sportscar'
        case _:
            return 'Not a sportscar'


# def sportcars(car):
#     if car == 'Ferrari' or car == 'Lamborghini' or car == 'Porsche' or car == 'Aston Martin':
#         return 'Sportscar'
#     else:
#         return 'Not a sportscar'




print(sportcars('Ferrari'))  # multiple cases with OR condition will return Sportscar
print(sportcars('Fiat'))  # multiple cases with OR condition will return Not a sportscar
