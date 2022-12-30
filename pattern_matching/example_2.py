# devoriales.com, 2022
# Movie Menu
# Path: pattern_matching/example_2.py
# Description: Movie Menu using Structural Pattern Matching

# # movie menu with if else statements
# def movie_menu(movie):
#     # if else statements
#     if movie == '1':
#         return 'Loading The Matrix'
#     elif movie == '2':
#         return 'Loading The Avengers'
#     elif movie == '3':
#         return 'Loading The Dark Knight'
#     elif movie == '4':
#         return 'Loading The Godfather'
#     else:
#         return 'Loading Invalid Choice'

# movie menu with match statement
def movie_menu(movie):
    # switch case
    match movie:
        case '1':
            return 'Loading The Matrix'
        case '2':
            return 'Loading The Avengers'
        case '3':
            return 'Loading The Dark Knight'
        case '4':
            return 'Loading The Godfather'
        case _:
            return 'Loading Invalid Choice'


# movie dictionary
movies = {
    '1': 'The Matrix',
    '2': 'The Avengers',
    '3': 'The Dark Knight',
    '4': 'The Godfather',
}
print('Movie Menu', end='\n****************\n')
for key, value in movies.items():
    print(f'{key}: {value}')


input = input('Select movie to watch: ')
print(movie_menu(input))
