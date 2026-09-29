import pandas as pd 

def usage_tier(consumption, t_one, t_two, t_three):
    if consumption <= 100:
        return consumption * t_one
    elif consumption <= 300:
        return (100 * t_one) + ((consumption - 100) * t_two)
    else:
        return (100 * t_one) + (200 * t_two) + ((consumption - 300) * t_three)


def calculate_tier_rate(csv_path: str, tier_one: float, tier_two: float, tier_three: float, fixed_fee: float) -> float : 
    
    if not isinstance(csv_path, str):
        raise TypeError("CSV path must be provided or value must be a string.")
    if not isinstance(tier_one, float) or not isinstance(tier_two, float) or not isinstance(tier_three, float) or not isinstance(fixed_fee, float):
        raise TypeError("Fixed Fee or any type of Rates must be provided or value must be a float.")
    if fixed_fee < 0 or tier_one < 0 or tier_two < 0 or tier_three < 0:
        raise ValueError("Fixed Fee or any type of Rates must be same or higher than $0.00.")
    
    id = pd.read_csv(csv_path)

    id['kWh'] = id['kWh'].astype(float)

    total_consumption = id['kWh'].sum()

    if total_consumption < 0:
        raise ValueError("Usage must be same or higher than 0.00kWh.")

    total_consumption = usage_tier(total_consumption, tier_one, tier_two, tier_three)

    return round(total_consumption + fixed_fee, 2)
