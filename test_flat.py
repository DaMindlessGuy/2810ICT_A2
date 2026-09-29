import pytest
from contextlib import nullcontext
from pricing_models.flat_rate import calculate_flat_rate

class TestFlatRate:
    @pytest.mark.parametrize("path, fixed_rate, fixed_fee, expected, expectation", [
        # typical testing 
        ("testing_data/typical_test_data.csv", 1.0, 10.0, 860.67, nullcontext()), # 850.67kWh
        ("testing_data/typical_test_data.csv", 0.25, 10.0, 222.67, nullcontext()),
        ("testing_data/typical_test_data.csv", 0.25, 25.0, 237.67, nullcontext()),
        # boundary testing
        ("testing_data/boundary_testing_data_3.csv", 1.0, 10.0, 10.00, nullcontext()),
        ("testing_data/typical_test_data.csv", 0.0, 10.0, 10, nullcontext()),
        ("testing_data/typical_test_data.csv", 1.0, 0.0, 850.67, nullcontext()),
                #invaild testing
        ("testing_data/invalid_testing_data_1.csv", 0.25, 10.0, 10.0, pytest.raises(ValueError)), #-15kWh
        ("testing_data/typical_test_data.csv", -1.0, 0.30, 0.40, pytest.raises(ValueError)), 
        ("testing_data/typical_test_data.csv", 0.20, -15.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", True, 0.30, 10.0, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.30, "True", 80, pytest.raises(TypeError)),
        (True, 0.20, 0.30, 0.40, pytest.raises(TypeError)), 
        (1234, 0.20, 0.30, 0.40, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", None, 0.30, 10.0, pytest.raises(TypeError)),
        ("testing_data/typical_test_data.csv", 0.20, None, 80, pytest.raises(TypeError)),
        (None, 0.20, 0.30, 0.40, pytest.raises(TypeError)),
        ])
    
    def test_flat_rate(self, path, fixed_rate, fixed_fee, expected, expectation):
        with expectation:
            assert calculate_flat_rate(path, fixed_rate, fixed_fee) == expected
