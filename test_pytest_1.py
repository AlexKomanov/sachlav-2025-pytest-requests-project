import pytest

a = 2
b = 3
c = 6
def test_calculate_sum_of_2_numbers():
    assert 2 + 3 == 5
    print("\nTest case executed successfully")
#
# def test_calculate_sum_of_2_numbers_error():
#     assert 2 + 3 == 6

# def test_calculate_sum_of_2_numbers_error_with_values():
#     assert a + b == c

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 2 / 0

    assert "division by zero" in str(e.value)