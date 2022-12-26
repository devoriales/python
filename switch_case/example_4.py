# devoriales.com, 2022
# Path switch_case/check_http_status.py
# check http status codes


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
