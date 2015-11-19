#!/usr/bin/env python3

""" Module to test lab3.py """

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_OR_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31


# Write a test function for the months with 30 days
def test_months_with_30():
    """
    Test months with 30 days
    """
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30


# Write a test function for the months with 28 or 29 days
def test_months_with_28_or_29():
    """
    Test months with February
    """
    for item in MONTHS_WITH_28_OR_29:
        assert days_in_month(item) == "28 or 29"


# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method


def test_months_not_capitalized_properly():
    """
    Test months with months that are not capitalized properly

    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item.lower()) == 31


# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input
def test_unexpected_input_number():
    """
    Test with unexpected input, for example 4
    """
    try:
        days_in_month("23")
    except ValueError:
        assert True


def test_unexpected_input_string():
    """
    Test with unexpected input, for example a string other than a month
    """
    try:
        days_in_month(23)
    except AttributeError:
        assert True
