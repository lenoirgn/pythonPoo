#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`compare` module
:author: FIL - FST - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2016, january
:dernière révision: février 2026

Fonctions nécessaires au TP sur l'analyse des tris
"""
from typing import TypeVar
from functools import cmp_to_key
from typing import Callable, TypeVar
A = TypeVar('A')

def compare(x: A, y: A) -> int:
    """ Renvoie :
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    Précondition : x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, ==
         peuvent s'appliquer
    Exemple(s) :
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

def tri_python(liste: list[A], comp: Callable[[A, A], int] = compare) -> None:
    """ Adapte la méthode sort de Python aux paramètres de fonctions de tri au TP

    Précondition :
    Exemple(s) :
    $$$ liste = [3, 1, 4, 1, 5, 9, 2]
    $$$ tri_python(liste)
    $$$ liste == [1, 1, 2, 3, 4, 5, 9]
    True
    """
    liste.sort(key=cmp_to_key(comp))

def compare_deuxieme(x, y):
    """ Renvoie :
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    Précondition : x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, ==
         peuvent s'appliquer
    Exemples:
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
    apl1test.testmod('annexe_tris.py')
