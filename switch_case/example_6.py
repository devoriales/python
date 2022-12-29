# devoriales.com, 2022
# Path: switch_case/example_6.py
# description: multiple cases with AND condition


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
def sportcars(*car):
    if car[0] == 'Ferrari' and car[1] == 'Lamborghini':
        return 'Sportscars'
    else:
        return 'Not a sportscar'

    

print(sportcars('Ferrari', 'Lamborghini'))  # multiple cases with AND condition will return Sportscars
print(sportcars('Fiat', 'Lamborghini'))  # multiple cases with AND condition will return Not a sportscar

