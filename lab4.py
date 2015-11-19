#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it
PROVINCIAL_TAX_RATE = 0.05
FEDERAL_TAX_RATE = 0.025


def calc_provincial_tax(amount):
    provincial_tax = amount*PROVINCIAL_TAX_RATE
    return provincial_tax


def calc_federal_tax(amount):
    federal_tax = amount*FEDERAL_TAX_RATE
    return federal_tax


def calc_total_tax(provincial_tax, federal_tax):
    total_tax = provincial_tax + federal_tax
    return total_tax


def calc_subtotal(amount, total_tax):
    sub_total = amount + total_tax
    return sub_total


def bill_of_sale(purchase):

    provincial_tax = calc_provincial_tax(purchase)
    federal_tax = calc_federal_tax(purchase)
    total_tax = calc_total_tax(provincial_tax, federal_tax)
    subtotal = calc_subtotal(purchase, total_tax)

    with open("bill_of_sale.txt", "w") as file_container:

        file_container.write("Amount of purchase: {0:.2f} \n".format(purchase))
        file_container.write("Provincial tax: {0:.2f} \n".format(provincial_tax))
        file_container.write("Federal tax: {0:.2f} \n".format(federal_tax))
        file_container.write("Total tax: {0:.2f} \n".format(total_tax))
        file_container.write("Total sale: {0:.2f} \n".format(subtotal))

bill_of_sale(100)