
import pandas as pd

def calculate_tou_rate(csv_path: str, fixed_fee: float, peak_rate: float, off_peak_rate: float, shoulder_rate: float) -> float:

    if not isinstance(csv_path, str):
        raise TypeError("CSV path must be provided or value must be a string.")
    if not isinstance(fixed_fee, float) or not isinstance(peak_rate, float) or not isinstance(off_peak_rate, float) or not isinstance(shoulder_rate, float):
        raise TypeError("Fixed Fee or any type of Rates must be provided or value must be a float.")
    if fixed_fee < 0 or peak_rate < 0 or off_peak_rate < 0 or shoulder_rate < 0:
        raise ValueError("Fixed Fee or any type of Rates must be same or higher than $0.00.")

    # Grab dataset
    id = pd.read_csv(csv_path)

    # Map out the dataframe to desired format

    id['timestamp'] = pd.to_datetime(id['timestamp']) # converting the timestamp column into datetime format for further processing

    id.set_index('timestamp', inplace=True) # setting dataframe index

    peak_id = id.between_time('18:00:00', '21:59:59') # peak rate includes the hours from 6pm to 10pm, applying filter to get the peak usage

    off_id = id.between_time('22:00:00', '06:59:59') # off peak rate includes the hours from 10pm to 7am, applying filter to get the off peak usage

    shoulder_id = id.between_time('07:00:00', '17:59:59') # shoulder rate includes the hours from 7am to 6pm, applying filter to get the shoulder usage

    # Sum calculation of the kWh values for each usage type

    peak_sum = peak_id['kWh'].sum() # summing the kWh values for the peak usage

    off_peak_sum = off_id['kWh'].sum() # summing the kWh values for the off peak usage

    shoulder_sum = shoulder_id['kWh'].sum() # summing the kWh values for the shoulder usage

    if peak_sum < 0 or off_peak_sum < 0 or shoulder_sum < 0:
        raise ValueError("Usage must be same or higher than 0.00kWh.")

    #------

    total_bill = 0
    total_bill += peak_rate * peak_sum
    total_bill += off_peak_rate * off_peak_sum
    total_bill += shoulder_rate * shoulder_sum
    total_bill += fixed_fee

    return round(total_bill, 2)
