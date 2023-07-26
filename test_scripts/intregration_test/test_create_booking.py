'''
Author : Dipak
Objective : Create and Verify by Post Request
TC#1 - Verify The Status Code, Header
TC#2 - Verify the Body -> Booking ID
TC#3 - Verify the JSON Schema is Valid
'''

import pytest
from src.constants.apicontanst import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.common_verification import verify_http_code, verify_key
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers import *


class TestIntregration(object):

    # Payload
    # Base Url
    # Verify

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), auth=None, headers=common_headers(),
                                payload=payload_create_booking(), in_json=False)

      #  verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(response, booking_id)
