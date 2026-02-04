def test_add_accum_with_value_5(accum):
    accum.add_accum(5)
    assert accum.count == 5

def test_add_accum_with_value_10(accum):
    accum.add_accum(10)
    assert accum.count == 10

def test_add_accum_with_value_0(accum):
    accum.add_accum(0)
    assert accum.count == 0