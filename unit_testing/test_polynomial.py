from polynomial import Polynomial


def test_if_polynomial_summation_is_correct():
    first_polynomial = Polynomial([3, -2, -1, 16], 3)
    second_polynomial = Polynomial([5, -10], 1)
    expected_polynomial_from_sum = Polynomial([3, -2, 4, 6], 3)

    result_polynomial_from_sum = first_polynomial + second_polynomial

    assert result_polynomial_from_sum.coefs == expected_polynomial_from_sum.coefs
    assert result_polynomial_from_sum.order == expected_polynomial_from_sum.order


def test_if_polynomial_subtraction_is_correct():
    first_polynomial = Polynomial([3, -2, -1, 16], 3)
    second_polynomial = Polynomial([5, -10], 1)
    expected_polynomial_from_sum = Polynomial([3, -2, -6, 26], 3)

    result_polynomial_from_sum = first_polynomial - second_polynomial

    assert result_polynomial_from_sum.coefs == expected_polynomial_from_sum.coefs
    assert result_polynomial_from_sum.order == expected_polynomial_from_sum.order


def test_if_polynomial_multiplication_is_correct():
    first_polynomial = Polynomial([1, 5, 1, -5], 3)
    second_polynomial = Polynomial([7, 7, 7], 2)
    expected_polynomial_from_sum = Polynomial([7, 42, 49, 7, -28, -35], 5)

    result_polynomial_from_sum = first_polynomial * second_polynomial

    assert result_polynomial_from_sum.coefs == expected_polynomial_from_sum.coefs
    assert result_polynomial_from_sum.order == expected_polynomial_from_sum.order


def test_if_polynomial_print_is_working_correctly():
    test_polynomial = Polynomial([7, 7, 7], 2)
    expected_polynomial_as_str = "7x**2 + 7x**1 + 7"

    assert str(test_polynomial) == expected_polynomial_as_str
