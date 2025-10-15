from discriminant.calc import discriminant, roots_info


def test_discriminant_negative_complex_roots():
    d = discriminant(1, 1, 1)
    assert d == -3
    info, d2 = roots_info(1, 1, 1)
    assert info == "complex"
    assert d2 == -3
