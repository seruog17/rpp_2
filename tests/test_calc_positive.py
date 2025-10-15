from discriminant.calc import discriminant, roots_info


def test_discriminant_positive_two_roots():
    d = discriminant(1, -5, 6)
    assert d == 1
    info, d2 = roots_info(1, -5, 6)
    assert info == "two"
    assert d2 == 1


def test_discriminant_zero_one_root():
    assert discriminant(1, -2, 1) == 0
    info, d = roots_info(1, -2, 1)
    assert info == "one"
    assert d == 0
