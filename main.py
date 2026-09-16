#!/usr/bin/env python

from pricing_models.flat_rate import calculate_flat_rate
from pricing_models.tou_rate import calculate_tou_rate
from pricing_models.tier_rate import calculate_tier_rate

CSV_PATH = "./sample_usage_data_month.csv"

if __name__ == "__main__":

    fixed_fee = 10.0
    flat_rate_price = calculate_flat_rate(CSV_PATH, 0.25, fixed_fee)
    tou_rate_price = calculate_tou_rate(CSV_PATH, fixed_fee)
    tier_rate_price = calculate_tier_rate(CSV_PATH, 0.20, 0.30, 0.40, fixed_fee)


    print(f"Flat rate price is {round(flat_rate_price, 2)}")
    print(f"Time of Use price is {round(tou_rate_price, 2)}")
    print(f"Tiered rate price is {round(tier_rate_price, 2)}")

