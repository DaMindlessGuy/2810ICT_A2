from pricing_models.tier_rate import calculate_tier_rate
import pytest
from contextlib import nullcontext


class TestTierRate:
    @pytest.mark.parametrize("path, tier_one, tier_two, tier_three, fixed_fee, expected, expectation", [
        # typical testing 
        ("testing_data/boundary_testing_data_1.csv", 0.20, 0.00, 0.0, 10.0, 15.57, nullcontext()), # 27.86kWh
        ("testing_data/boundary_testing_data_2.csv", 0.0, 0.30, 0.0, 10.0, 38.60, nullcontext()), # 195.33kWh
        ("testing_data/typical_test_data.csv", 0.0, 0.0, 0.40, 10.0, 230.27, nullcontext()), # 850.67kWh
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, 10.0, 310.27, nullcontext()), 
        # boundary testing
        ("testing_data/boundary_testing_data_3.csv", 0.20, 0.30, 0.40, 10.0, 10.0, nullcontext()),  # 0kWh
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, 0.0, 300.27, nullcontext()), 
        ("testing_data/typical_test_data.csv", 0.0, 0.30, 0.40, 0.0, 280.27, nullcontext()),
        ("testing_data/typical_test_data.csv", 0.20, 0.00, 0.40, 0.0, 240.27, nullcontext()),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.0, 0.0, 80, nullcontext()),

        ("testing_data/boundary_testing_data_13.csv", 0.20, 0.30, 0.40, 0.0, 19.87, nullcontext()), #99.36kWh
        ("testing_data/boundary_testing_data_14.csv", 0.20, 0.30, 0.40, 0.0, 20.28, nullcontext()), #100.93kWh
        ("testing_data/boundary_testing_data_15.csv", 0.20, 0.30, 0.40, 0.0, 79.77, nullcontext()), #299.22kWh
        ("testing_data/boundary_testing_data_16.csv", 0.20, 0.30, 0.40, 0.0, 80.80, nullcontext()), #301.99kWh
        #invaild testing
        ("testing_data/invalid_testing_data_1.csv", 0.20, 0.30, 0.40, 10.0, 10.0, pytest.raises(ValueError)), #-15kWh        
        ("testing_data/typical_test_data.csv", -1.0, 0.30, 0.40, 0.0, 80, pytest.raises(ValueError)), 
        ("testing_data/typical_test_data.csv", 0.20, -2.0, 0.40, 0.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, -3.0, 0.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, -15.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", True, 0.30, 0.40, 10.0, 10.0, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, "False", 0.40, -15.0, 80, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, False, -15.0, 80, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, "True", 80, pytest.raises(TypeError)),
        (True, 0.20, 0.30, 0.40, 10.0, 10.0, pytest.raises(TypeError)), 
        (1234, 0.20, 0.30, 0.40, 10.0, 10.0, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", None, 0.30, 0.40, 10.0, 10.0, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, None, 0.40, -15.0, 80, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, None, -15.0, 80, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, None, 80, pytest.raises(TypeError)),
        (None, 0.20, 0.30, 0.40, 10.0, 10.0, pytest.raises(TypeError)),
    ])
    def test_tier_rate(self, path, tier_one, tier_two, tier_three, fixed_fee, expected, expectation):
        with expectation:
            assert calculate_tier_rate(path, tier_one, tier_two, tier_three, fixed_fee) == expected

