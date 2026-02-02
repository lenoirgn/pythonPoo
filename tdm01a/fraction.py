#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
`fraction` module : fraction representation

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2024, january. Last revision: 2024, january

"""
from __future__ import annotations
import math
from typing import Self
from math import lcm, floor, sqrt

class Fraction:
    """
    a class for rational numeratorbers.

    $$$ f1 = Fraction(2, 3)
    $$$ f1.denominator
    3
    $$$ f1.numerator
    2
    $$$ f2 = Fraction(5, 7)
    $$$ f1 * f2 == Fraction(10, 21)
    True
    $$$ f1 + f2 == Fraction(29, 21)
    True
    $$$ f1 - f2 == Fraction(-1, 21)
    True
    $$$ str(f1)
    '2/3'
    """

    def __init__(self, numerator: int, denominator: int):
        """
        initialize the new fraction numerator/précondition.

        denominator: denominator != 0
        """
        assert denominator !=0, "denominator different de 0"
        self.numerator = numerator
        self.denominator = denominator
        

    def __str__(self) -> str:
        """
        return a new string representation of this fraction.

        precondition: aucune

        exemples:
        $$$ str(Fraction(22, 7))
        '22/7'
        """
        return f"{self.numerator}/{self.denominator}"

    def repr(self) -> str:
        """
        return a litteral representation of this object.
        """
        return f"Fraction({self.numerator},{self.denominator})"

    def __eq__(self, other) -> bool:
        """
        return True if and only if self and other are two equals fractions.

        precondition: none

        exemples:
        $$$ Fraction(2, 7) == Fraction(6, 21)
        True
        $$$ Fraction(2, 7) == Fraction(5, 21)
        False
        """
        return self.numerator*other.denominator == self.denominator*other.numerator

    def __add__(self, other) -> Self:
        """
        return a fraction representing self + other.

        precondition: aucune

        exemples:
        $$$ Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
        True
        """
        res_denominator=lcm(self.denominator,other.denominator)
        res_numerator=self.numerator*(res_denominator//self.denominator)+other.numerator*(res_denominator//other.denominator)
        return Fraction(res_numerator,res_denominator)

    def inverse(self) -> Self:
        """Return inverse of a fraction.

        précondition: self != 0

        exemples :
        $$$ Fraction(4, 3).inverse()
        Fraction(3, 4)
        $$$ Fraction(21, 15).inverse()
        Fraction(5, 7)
        """
        return Fraction(self.denominator,self.numerator)

    def __truediv__(self, other) -> Self:
        """Return divisions of two fractions.

        précondition : other != 0

        exemples :
        """
        assert other!=0,"le diviseur doit etre different de 0"
        inverse_other=other.inverse()

        return self*inverse_other
    def __mul__(self, other):
        """
        return a fraction representing self * other.

        precondition: aucune

        exemples:
        $$$ Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
        True
        """
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)

    def __neg__(self):
        """
        return the negate of self.

        precondition: aucune

        exemples:

        $$$ -Fraction(2, 7) == Fraction(-2, 7)
        True
        """
        if self.denominator > 0:
            return Fraction(-self.numerator, self.denominator)
        return Fraction(self.numerator, -self.denominator)

    def __sub__(self, other):
        """
        return a fraction representing self - other.

        precondition: aucune

        exemples:
        $$$ Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
        True
        """
        return self+(-other)

    def __repr__(self) -> str:
        """
        return the litteral expression of self.
        """
        return f"Fraction({self.numerator},{self.denominator})"

    def to_float(self) -> float:
        """
        Return an approximated float value.

        précondition: \

        exemples :

        $$$ Fraction(0, 4).to_float()
        approx(0, 4)
        $$$ Fraction(1, 4).to_float()
        approx(1/4, 4)
        $$$ Fraction(1, 6).to_float()
        approx(0.1667, 4)
        """
        return self.numerator/self.denominator


def racine_entiere(a: int) -> int:
    """Renvoie la racine carré entière de a.

    C'est-à-dire l'entier r vérifiant r² <= a < (r+1)²

    précondition : a >= 0

    exemple :

    $$$ racine_entiere(0)
    0
    $$$ racine_entiere(150)
    12
    $$$ racine_entiere(9)
    3
    """
    return floor(sqrt(a))


def heron(a: int, p: int) -> Fraction:
    """Renvoie la fraction obtenue après p itérations de la méthode de Héron.

    précondition : a >= 0 and p >= 0

    exemple :

    $$$ heron(0, 0)
    Fraction(0, 1)
    $$$ heron(2, 0)
    Fraction(1, 1)
    $$$ heron(2, 1)
    Fraction(3, 2)
    $$$ heron(2, 3)
    Fraction(577, 408)
    $$$ heron(2, 5)
    Fraction(886731088897, 627013566048)
    """
    if a==0:
        return Fraction(0,1)
    x=Fraction(1,1)
    
    for _ in range(p):
        x=(x+Fraction(a,1)/x)/Fraction(1,2)
        
    return x


if __name__ == '__main__':
    import l1test
    l1test.testmod('fraction.py')

