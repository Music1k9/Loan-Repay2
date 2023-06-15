# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:43:09 2023

@author: nlewisbassett
"""

def compute_monthly_repayment(PV, r, n):
    # Convert APR to monthly interest rate
    monthly_interest_rate = r / (12 * 100)

    # Calculate monthly repayment amount
    numerator = PV * monthly_interest_rate
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    monthly_repayment = numerator / denominator

    return monthly_repayment

# Example usage
PV = 12000
r = 7.45
n = 48

monthly_repayment_amount = compute_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount: $", round(monthly_repayment_amount, 2))
