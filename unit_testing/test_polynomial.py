from polynomial import Polynomial

def test_if_polynomial_summation_is_correct():
    first_polynomial = Polynomial([3, -2, -1, 16], 3)
    second_polynomial = Polynomial([5, -10], 1)
    expected_polynomial_from_sum = Polynomial([3, -2, 4, 6], 3)

    result_polynomial_from_sum = first_polynomial + second_polynomial

    assert result_polynomial_from_sum.coefs == expected_polynomial_from_sum.coefs
    assert result_polynomial_from_sum.order == expected_polynomial_from_sum.order
