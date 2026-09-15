'''

Total consumption calculation requires turning each 1 hour value into one day's total consumption,
then summing all the daily totals for the month. Considering the data value is the CSV file in format of
timestamp (yyyy-mm-dd hh:mm:ss; where only hours are changinging within the day (24 rows)) and kW/h value (float).

While researching via Google, found the ideal library to use, which is Pandas.
Separate testing will be conducte on other file.

'''

"""

--Draft version

# Single fixed price per unit of electricity (kW/h) tariff model

fp = 0.25 # fixed price of electricity per month

fx = 10.0 # fixed fee for each tariff model

tc = 300 # total consumption in kW/h per month, temporary value for testing

# calculation model

tb = (tc * fp) + fx # total bill for the month

print("Total bill for this month is: $", tb)

"""
import pandas as pd #importing pandas library

id = pd.read_csv('./sample_usage_data_month.csv')

id['kWh'] = id['kWh'].astype(float)

tc = id['kWh'].sum()

print(tc) #Sanity check, will be deleted on production

#User can add values, may differnt in testing with pytest; can be removed on production, where values will be hardcoded.
fp = float(input("What is the fixed price of electricity per month? (in $/kWh): ")) 

fx = float(input("What is the fixed fee for this tariff model? (in $): "))

# calculation model

tb = (tc * fp) + fx # total bill for the month

print("Total bill for this month is: $", round(tb), 2)