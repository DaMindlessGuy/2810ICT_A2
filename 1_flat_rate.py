'''

Total consumption calculation requires turning each 1 hour value into one day's total consumption,
then summing all the daily totals for the month. Considering the data value is the CSV file in format of
timestamp (yyyy-mm-dd hh:mm:ss; where only hours are changinging within the day (24 rows)) and kW/h value (float).

While researching via Google, found the ideal library to use, which is Pandas.
Separate testing will be conducte on other file.

'''

# Single fixed price per unit of electricity (kW/h) tariff model

fp = 0.25 # fixed price of electricity per month

fx = 10.0 # fixed fee for each tariff model

tc = 300 # total consumption in kW/h per month, temporary value for testing

# calculation model

tb = (tc * fp) + fx # total bill for the month

print("Total bill for this month is: $", tb)
