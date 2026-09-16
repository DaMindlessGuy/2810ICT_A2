import pandas as pd #importing pandas library

#essential codes to feed data
id = pd.read_csv('./sample_usage_data_month.csv') # reading the csv file within the same repository, hardcoded path.
# it may require different method for production, where file is always named in specific format.
#------



id['timestamp'] = pd.to_datetime(id['timestamp']) # converting the timestamp column into datetime format for further processing

db = id.groupby(id['timestamp'].dt.date) # grouping the data by date, automatic grouping of 24 rows on the day

id.set_index('timestamp', inplace=True) # setting dataframe index



"""
Random testing codes
---
for day, group in db:
    print(f"Date: {day}")
    print(group)
# this code prints the date of the dataset and prints the 24 rows of data for that day

fixed rate testing codes (Complete)

# total sum of kWh for the month
id['kWh'] = id['kWh'].astype(float) # converting the kWh column into float format for further processing

ss = id['kWh'].sum() # summing the kWh values for the month, this is the total consumption in kWh for the month

print(ss) # current outcome is 850.67, where it has been verified with given CSV file.

print(f"Total consumption for the month is: {ss} kWh") # printing the total consumption for the month
#------

peak_id = id.between_time('18:00', '22:00') # applying filter to get the peak usage

peak_group = peak_id.groupby(peak_id.index.date) # grouping the peak usage by date

peak_sum = peak_id['kWh'].sum() # summing the kWh values for the peak usage

print(f"Total peak consumption for the month is: {round(peak_sum, 2)} kWh") # printing the total peak consumption for the month

for day, group in peak_group:
    print(f"Date: {day}")
    print(group)
# sanity check, printing all days with selected peak usage time, will be removed on production

"""