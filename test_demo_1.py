# Just to present naming convension of test file naming and structure
import pytest

@pytest.mark.basics
def test_example_1():
    pass

# incorrect named test function
def example_test():
    pass

# incorrect named test function
def validate_test_case():
    pass

@pytest.mark.basics
def test_example_2():
    pass