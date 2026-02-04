from source.accumulator import Accumulator
import pytest

@pytest.fixture()
def accum():
    print("\nlocal fixture")
    return Accumulator()


def test_initial_count_is_zero(accum):
    assert accum.count == 0

def test_add_accum_default(accum):
    accum.add_accum()
    assert accum.count == 1

