from __future__ import annotations
from typing import Union, List


class Polynomial:
    def __init__(self, coefs: List[Union[int, float]], order: int):
        # Coefficients from x**order to x**0 (constant coefficient)
        # If there is a x**n which has no coefficient between x**order
        # and x**0 or if no constant, the coefficients must be set to 0 in
        # the list.
        # List size is order + 1 (constant coef)
        self.coefs = coefs
        self.order = order

    def __add__(self, other_polynomial: Polynomial) -> Polynomial:
        if self.order != other_polynomial.order:
            polynomial_a, other_polynomial = self.make_polynomials_match_order(
                Polynomial(self.coefs, self.order), other_polynomial
            )
            self.coefs = polynomial_a.coefs
            self.order = polynomial_a.order
        for index in range(self.order + 1):
            self.coefs[index] = self.coefs[index] + other_polynomial.coefs[index]

        return Polynomial(self.coefs, self.order)

    def make_polynomials_match_order(
        self, polynomial_a: Polynomial, polynomial_b: Polynomial
    ) -> tuple[Polynomial]:
        if polynomial_a.order > polynomial_b.order:
            polynomial_a, polynomial_b = self.fill_right_polynomial(
                polynomial_a, polynomial_b
            )
            polynomial_b.order = polynomial_a.order
        if polynomial_a.order < polynomial_b.order:
            polynomial_a, polynomial_b = self.fill_left_polynomial(
                polynomial_a, polynomial_b
            )
            polynomial_a.order = polynomial_b.order
        return (polynomial_a, polynomial_b)

    def fill_left_polynomial(
        self, polynomial_a: Polynomial, polynomial_b: Polynomial
    ) -> tuple[Polynomial]:
        fill_with_zero_counter = 0
        order_difference = polynomial_b.order - polynomial_a.order
        while fill_with_zero_counter < order_difference:
            polynomial_a.coefs.insert(0, 0)
            fill_with_zero_counter += 1
        return (polynomial_a, polynomial_b)

    def fill_right_polynomial(
        self, polynomial_a: Polynomial, polynomial_b: Polynomial
    ) -> tuple[Polynomial]:
        fill_with_zero_counter = 0
        order_difference = polynomial_a.order - polynomial_b.order
        while fill_with_zero_counter < order_difference:
            polynomial_b.coefs.insert(0, 0)
            fill_with_zero_counter += 1
        return (polynomial_a, polynomial_b)
