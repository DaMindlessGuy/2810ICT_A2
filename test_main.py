
import pytest
from pricing_models.flat_rate import calculate_flat_rate
from pricing_models.tou_rate import calculate_tou_rate
from pricing_models.tier_rate import calculate_tier_rate

# Epsilon is here because of floating point math
# For example: `assert 0.1 + 0.2 == 0.3` does not work whereas
# `assert abs( (0.1 + 0.2) - (0.3) ) <= EPSILON` works
EPSILON = 0.001

class TestFlatRate:
    # flat_rate_price = calculate_flat_rate(CSV_PATH, 0.25, fixed_fee)
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee, expected", [
        ("testing_data/testing_data.csv", 1.0, 0.0,   3.73), 
        ("testing_data/testing_data.csv", 1.0, 10.0, 13.73), 
        ("testing_data/testing_data.csv", 2.0, 0.0,   7.46), 
        ])
    def test_flat_rate(self, path, fixed_rate, fixed_fee, expected):
        assert abs(calculate_flat_rate(path, fixed_rate, fixed_fee) - expected) <= EPSILON
