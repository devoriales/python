# devoriales.com, 2022
# Movie Streming Service
# Path: switch_class.py
# Description: Switch statement in Python using class method

class Movie():

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    @classmethod
    def get_movie(cls, option: int):
        match option:
            case 1:
                return cls('The Matrix', 1999, 8.7)
            case 2:
                return cls('The Avengers', 2012, 8.1)
            case 3:
                return cls('The Dark Knight', 2008, 9.0)
            case 4:
                return cls('The Godfather', 1972, 9.2)
            case _:
                return cls('Invalid Choice', 0, 0)

    def __str__(self):        
        return f'Name: {self.name} Year: {self.year} - Rating: {self.rating}'


# movie class instance 


movies = {
    '1': 'The Matrix',
    '2': 'The Avengers',
    '3': 'The Dark Knight',
    '4': 'The Godfather',
}

if __name__ == '__main__':

    # Presenting a movie menu
    print('Movie Menu', end='\n****************\n')
    for key, value in movies.items():
        print(f'{key}: {value}')

    # Get user input
    input = input('Select movie to watch: ')

    # Create a movie class instance from the alternative constructor
    movie = Movie.get_movie(int(input))

    print(movie) # print movie details from our class instance
