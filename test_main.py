
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

        ("testing_data/typical_test_data.csv", 1.0, 10.0, 860.67),
        ("testing_data/typical_test_data.csv", 1.0, 0.0, 850.67),
        ("testing_data/typical_test_data.csv", 0.25, 10.0, 222.67),
        ("testing_data/typical_test_data.csv", 0.25, 25.0, 237.67),
        
        ("testing_data/boundary_testing_data_1.csv", 1.0, 0.0, 27.86), 
        ("testing_data/boundary_testing_data_2.csv", 1.0, 0.0, 195.33),
        ("testing_data/boundary_testing_data_3.csv", 1.0, 10.0, 10.00),

        pytest.param(True, 1.0, 10.0, 0, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(1234, 1.0, 0.0, 0, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param("testing_data/typical_test_data.csv", -1.0, 10.0, 0, marks=pytest.mark.xfail(raises=ValueError)),
        pytest.param("testing_data/typical_test_data.csv", 1.0, -15.0, 0, marks=pytest.mark.xfail(raises=ValueError)), 
        pytest.param(None, 1.0, 10.0, 0, marks=pytest.mark.xfail(raises=TypeError)),  
        ])
    
    def test_flat_rate(self, path, fixed_rate, fixed_fee, expected):
        assert (calculate_flat_rate(path, fixed_rate, fixed_fee) - expected) <= EPSILON

"""

class TestTOURate:
    @pytest.mark.parametrize("path, fixed_fee, expected", [
        ("testing_data/testing_data.csv", 0.0, 0.0),
        ("testing_data/testing_data.csv", 10.0, 0.0),
        ("testing_data/testing_data.csv", 0.0, 0.0), #requries manual calcuated expected output
    ])
    def test_tou_rate(self, path, fixed_fee, expected):
        assert abs(calculate_tou_rate(path, fixed_fee)) - expected <= EPSILON
    # for edge case testing, create new testing data that has times of use at turning points. TODO

class TestTierRate:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee, expected", [
        ("testing_data/testing_data.csv", 0.20, 0.30, 0.40, 0.0, 0.0),
        ("testing_data/testing_data.csv", 0.20, 0.30, 0.40, 10.0, 0.0),
        ("testing_data/testing_data.csv", 0.20, 0.30, 0.40, 0.0, 0.0), #requries manual calcuated expected output
    ])
    def test_tier_rate(self, path, tier_one, tier_two, tier_three, fixed_fee, expected):
        assert abs(calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee)) - expected <= EPSILON
        
"""