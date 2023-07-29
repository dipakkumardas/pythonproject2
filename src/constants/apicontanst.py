# Add your constants here

# Adding my URL constants. Python -> functions

def base_url():
    # Change bases on the env.json - Stage , prepared, prod
    # In Future I will write a logic to change the base url based on the env
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id
