#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`compare` module
:author: FIL - FST - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2016, january
:dernière révision: février 2018

Fonctions de comparaison 
pour l'analyse des algos de recherche et de tri

"""
from abc import abstractmethod
from functools import wraps

class A:

    @abstractmethod
    def __eq__(self, other) -> bool:
        ...

    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

def compare(x: A, y: A) -> int:
    """
    Renvoie :
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    précondition: x et y doivent être d'un type pour lequel les opérateurs
         de comparaison <, <=, == peuvent s'appliquer
    exemples:

    $$$ compare(1, 3)
    -1
    $$$ compare(3, 1)
    1
    $$$ compare(3, 3)
    0
    """
    if x == y:
        return 0
    elif x > y:
        return 1
    else:
        return -1
def not_compare(x: A, y: A) -> int:
    """
    Renvoie :
      - 1 si x < y
      - 0 si x == y
      - -1 si x > y
    précondition: x et y doivent être d'un type pour lequel les opérateurs
         de comparaison <, <=, == peuvent s'appliquer
    exemples:

    $$$ not_compare(1, 3)
    1
    $$$ not_compare(3, 1)
    -1
    $$$ not_compare(3, 3)
    0
    """
    if x == y:
        return 0
    elif x > y:
        return -1
    else:
        return 1

def compare_deuxieme(x, y):
    """
    renvoie :
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    précondition: x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, ==
         peuvent s'appliquer
    exemples:

    $$$ compare_deuxieme((1,2), (3,4))
    -1
    $$$ compare_deuxieme((3, 2), (4, 1))
    1
    $$$ compare_deuxieme((3, 3),(3, 3))
    0
    """
    if x[1] < y[1]:
        res = -1
    elif x[1] > y[1]:
        res = 1
    else:
        res = 0
    return res

if (__name__ == '__main__'):
    import apl1test
    apl1test.testmod('compare.py')
