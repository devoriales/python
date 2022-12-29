# devoriales.com, 2022
# Path: switch_case/example_5.py
# description: benchmarking switch case vs if else in python


# match statement
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
