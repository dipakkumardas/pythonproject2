'''
Author : Dipak
Objective : Create and Verify by Post Request
TC#1 - Verify The Status Code, Header
TC#2 - Verify the Body -> Booking ID
TC#3 - Verify the JSON Schema is Valid
'''
import pytest


@pytest.mark.run(order=1)
def test_create_booking_tc1():
    assert True == True


@pytest.mark.run(order=2)
def test_create_booking_tc2():
    assert True == False


@pytest.mark.run(order=3)
def test_create_booking_tc3():
    assert True == True