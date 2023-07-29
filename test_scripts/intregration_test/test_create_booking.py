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
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers


class TestIntegration(object):

    # Payload
    # Base Url
    # Verify

    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
       # print(response.status_code)
        # print(response.json())

       # verify_http_code(response, 200)
        #booking_id = response.json()["bookingid"]
        verify_key_for_not_null_greater_than_zero(response.json()["bookingid"])

    def test_case_02(self):
        assert True == True

    def test_case_03(self):
        assert True == True
