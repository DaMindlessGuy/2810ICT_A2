import pandas as pd 

def usage_tier(consumption, one, two, three):
    if consumption <= 100:
        return consumption * one
    elif consumption <= 300:
        return (100 * one) + ((consumption - 100) * two)
    else:
        return (100 * one) + (200 * two) + ((consumption - 300) * three)


def calculate_tier_rate(csv_path: str, tier_one: float, tier_two: float, tier_three: float, fixed_fee: float) -> float : 

    id = pd.read_csv(csv_path)

    id['kWh'] = id['kWh'].astype(float)

    total_consumption = id['kWh'].sum()

    total_consumption = usage_tier(total_consumption, tier_one, tier_two, tier_three)

    return total_consumption + fixed_fee
