import pytest
from contextlib import nullcontext
from pricing_models.tou_rate import calculate_tou_rate

class TestTOURate:
    @pytest.mark.parametrize("path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected, expectation", [
        # typical testing
        ("testing_data/typical_test_data.csv", 10.0, 0.40, 0.0, 0.0, 116.87, nullcontext()), # 850.67kWh 
        ("testing_data/typical_test_data.csv", 10.0, 0.0, 0.15, 0.0, 37.87, nullcontext()), 
        ("testing_data/typical_test_data.csv", 10.0, 0.0, 0.0, 0.25, 109.43, nullcontext()),
        ("testing_data/typical_test_data.csv", 15.0, 0.40, 0.15, 0.25, 249.16, nullcontext()), 
        # boundary testing
        ("testing_data/boundary_testing_data_6.csv", 0.0, 0.40, 0.15, 0.25, 0.41, nullcontext()), #1.63 17:59:59
        ("testing_data/boundary_testing_data_7.csv", 0.0, 0.40, 0.15, 0.25, 0.71, nullcontext()), #1.77 18:00:00
        ("testing_data/boundary_testing_data_8.csv", 0.0, 0.40, 0.15, 0.25, 1.16, nullcontext()), #2.91 21:59:59
        ("testing_data/boundary_testing_data_9.csv", 0.0, 0.40, 0.15, 0.25, 0.38, nullcontext()), #2.55 22:00:00
        ("testing_data/boundary_testing_data_4.csv", 0.0, 0.40, 0.15, 0.25, 0.06, nullcontext()), #0.38 06:59:59
        ("testing_data/boundary_testing_data_5.csv", 0.0, 0.40, 0.15, 0.25, 0.29, nullcontext()), #1.17 07:00:00

        ("testing_data/boundary_testing_data_1.csv", 0.0, 0.40, 0.15, 0.25, 7.68, nullcontext()),
        ("testing_data/boundary_testing_data_10.csv", 0.0, 0.00, 0.15, 0.25, 0, nullcontext()),
        ("testing_data/boundary_testing_data_11.csv", 0.0, 0.40, 0.0, 0.25, 0, nullcontext()),
        ("testing_data/boundary_testing_data_12.csv", 0.0, 0.40, 0.15, 0.0, 0, nullcontext()),
        ("testing_data/boundary_testing_data_3.csv", 10.0, 0.40, 0.15, 0.25, 10.0, nullcontext()),
        # invaild testing
        ("testing_data/typical_test_data.csv", -1.0, 0.40, 0.15, 0.25, 0.41, pytest.raises(ValueError)), 
        ("testing_data/typical_test_data.csv", 0.20, -2.0, 0.40, 0.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, -3.0, 0.0, 80, pytest.raises(ValueError)),
        ("testing_data/typical_test_data.csv", 0.20, 0.30, 0.40, -15.0, 80, pytest.raises(ValueError)),
        ("testing_data/invalid_testing_data_1.csv", 0.20, 0.30, 0.40, 10.0, 10.0, pytest.raises(ValueError)), #-15kWh        
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
    def test_tou_rate(self, path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate, expected, expectation):
        with expectation:
            assert calculate_tou_rate(path, fixed_fee, peak_rate, off_peak_rate, shoulder_rate) == expected
