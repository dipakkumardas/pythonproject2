def payload_create_booking():
    # In future you can replace this from the excel or JSON
    payload = {
        "firstname": "David",
        "lastname": "Brown",
        "totalprice": 9999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    return payload
