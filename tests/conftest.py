from source.accumulator import Accumulator
import pytest

@pytest.fixture()
def accum():
    print("\nglobal fixture")
    return Accumulator()