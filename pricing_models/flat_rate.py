import pandas as pd 

def calculate_flat_rate(csv_path: str, fixed_price: float, fixed_fee: float) -> float: 
    """
    Users will define a csv_path, fixed_prive and fixed_fee and this will read the 
    given CSV with pandas and will multiply the usage per hour with the price per 
    hour, then returns that sum plus a fixed fee
    """

    if fixed_price < 0:
        raise ValueError("Fixed Rate must be same or higher than $0.00.")
    if fixed_fee < 0:
        raise ValueError("Fixed Fee must be same or higher than $0.00.")
    if not isinstance(csv_path, str):
        raise TypeError("CSV path must be provided or value must be a string.")
    
    id = pd.read_csv(csv_path)

    id['kWh'] = id['kWh'].astype(float)

    total_consumption = id['kWh'].sum()

    return (total_consumption * fixed_price) + fixed_fee
