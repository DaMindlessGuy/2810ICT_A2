"""
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

"""

import pandas as pd

def calculate_tou_rate(csv_path: str, fixed_fee: float) -> float:
    # Grab dataset
    id = pd.read_csv(csv_path)

    # Map out the dataframe to desired format

    id['timestamp'] = pd.to_datetime(id['timestamp']) # converting the timestamp column into datetime format for further processing

    id.set_index('timestamp', inplace=True) # setting dataframe index

    peak_id = id.between_time('18:00:00', '21:59:59') # applying filter to get the peak usage

    off_id = id.between_time('22:00:00', '06:59:59') # applying filter to get the off peak usage

    shoulder_id = id.between_time('07:00:00', '17:59:59') # applying filter to get the shoulder usage

    # the current filter is overlapping one hour on the boundary, may require further consultation or adding assumption

    #------

    # Sum calculation of the kWh values for each usage type
    peak_sum = peak_id['kWh'].sum() # summing the kWh values for the peak usage

    off_peak_sum = off_id['kWh'].sum() # summing the kWh values for the off peak usage

    shoulder_sum = shoulder_id['kWh'].sum() # summing the kWh values for the shoulder usage

    #------

    # Hardcoded rates; may need to consult whether this value has to be input via User

    peak_rate = 0.40

    # peak rate includes the hours from 6pm to 10pm
    off_peak_rate = 0.15

    # off peak rate includes the hours from 10pm to 7am
    shoulder_rate = 0.25 

    # shoulder rate includes the hours from 7am to 6pm

    #------

    #total_bill = (peak_rate * peak_sum) + (off_peak_rate * off_peak_sum) + (shoulder_rate * shoulder_sum) + fixed_fee

    total_bill = 0
    total_bill += peak_rate * peak_sum
    total_bill += off_peak_rate * off_peak_sum
    total_bill += shoulder_rate * shoulder_sum
    total_bill += fixed_fee

    return total_bill
    #print("Total bill for this month is: $", round(tb, 2))

    # Sanity check measures may be added to verify the calculation, consultation required
