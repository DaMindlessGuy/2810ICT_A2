import pandas as pd 

def calculate_flat_rate(csv_path: string, hourly_price: float, fixed_fee: float) -> float : 
    """
    Users will define a csv_path, fixed_prive and fixed_fee and this will read the 
    given CSV with pandas and will multiply the usage per hour with the price per 
    hour, then returns that sum plus a fixed fee
    """

    id = pd.read_csv(csv_path)

    id['kWh'] = id['kWh'].astype(float)

    total_consumption = id['kWh'].sum()

    return (total_consumption * hourly_price) + fixed_fee
