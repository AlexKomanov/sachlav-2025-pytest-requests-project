import pytest

test_data = [(2, 4, 6),
             (5, 7, 12),
             (10, 15, 25),
             (0, 0, 0),
             (-2, -3, -5),
             (10, -5, 5),
             (100, 200, 300)]

@pytest.mark.parametrize("num_1, num_2, expected_sum", test_data)
def test_sum_two_numbers(num_1: int, num_2: int, expected_sum: int):
    """Test to validate sum of two numbers."""
    assert num_1 + num_2 == expected_sum

