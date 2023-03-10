# devoriales.com, 2022
# Path : pattern_matching/example_4.py
# check http status codes using match statement


# switch case
def status_code(status_code):
    # switch case 
    match status_code:
        case 200:
            return 'OK'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:
            return 'Unknown'

print(status_code(500))  # check status code
