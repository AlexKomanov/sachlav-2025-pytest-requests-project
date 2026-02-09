import pytest

@pytest.mark.skip(reason="This test fails. Link to ticket: https://example.com/ticket/123")
@pytest.mark.accum
@pytest.mark.regression
def test_add_accum_with_value_5(accum):
    accum.add_accum(5)
    assert accum.count == 5

@pytest.mark.regression
@pytest.mark.accum
def test_add_accum_with_value_10(accum):
    accum.add_accum(10)
    assert accum.count == 10

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.accum
def test_add_accum_with_value_0(accum):
    accum.add_accum(0)
    assert accum.count == 0