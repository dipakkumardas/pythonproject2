# HTTP Status Code
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Expecetd HTTP Status" + expected_data

# Any Key should not be null or empty
def verify_key_for_not_null_greater_than_zero(key):
    assert key != 0, " Key is non Empty:" + key
    assert key > 0, " Key Should be greater then zero: " + key