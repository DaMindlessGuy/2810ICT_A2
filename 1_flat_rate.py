# Single fixed price per unit of electricity (kW/h) tariff model

fp = 0.25 # fixed price of electricity per month

fx = 10.0 # fixed fee for each tariff model

tc = 300 # total consumption in kW/h per month, temporary value for testing

# calculation model

tb = (tc * fp) + fx # total bill for the month

print("Total bill for this month is: $", tb)
