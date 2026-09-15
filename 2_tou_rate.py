'''

Total consumption calculation requires turning each 1 hour value into one day's total consumption,
then summing all the daily totals for the month. Considering the data value is the CSV file in format of
timestamp (yyyy-mm-dd hh:mm:ss; where only hours are changinging within the day (24 rows)) and kW/h value (float).

'''


pr = 0.40 # peak rate

# peak rate includes the hours from 6pm to 10pm

opr = 0.15 # off peak rate 

# off peak rate includes the hours from 10pm to 7am

sr = 0.25 # shoulder rate (All rates are $ per kWh)

# shoulder rate includes the hours from 7am to 6pm

pr_u = 100

opr_u = 80

sr_u = 120 # hardcoded values for testing; will be removed after data model is finalised

fx = 10.0 # fixed fee for each tariff model; the fee is estimated as $10 based on documentation

tb = (pr * pr_u) + (opr * opr_u) + (sr * sr_u) + fx # total bill for the month

print("Total bill for this month is: $", round(tb, 2))