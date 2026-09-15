import pandas as pd #importing pandas library

id = pd.read_csv('./sample_usage_data_month.csv') # reading the csv file within the same repository, hardcoded path.
# it may require different method for production, where file is always named in specific format.

print(id.head()) # prints the first 5 rows of the dataframe
