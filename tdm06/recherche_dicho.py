#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`recherches` module : un module pour les recherches

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2024 février

"""
from types import NoneType
from typing import Callable, TypeVar

# On définit un type générique :
C = TypeVar('C')


def indice_dicho(elem: C, liste: list[C], comp: Callable[[C, C], int]) \
                                    -> tuple[bool, int]:
    """Recherche l'élément `elem` dans la liste `liste`.

    Renvoie un couple (trouve, i) tel que:
        - si elem est un élément de liste,
             * trouve = True
             * i est l'indice de première occurence de elem dans liste
        - si elem n'est pas un élément de la liste :
             * trouve = False
             * pour tout j < i, liste[j] < liste[i]
             * pour tout j > i, liste[j] > liste[i]

    Précondition : comp est une fonction de comparaison et liste est triée pour comp

    $$$ def compare(x, y): return 0 if x == y else 1 if x > y else -1
    $$$ indice_dicho(0, [1, 3, 5], compare)
    (False, 0)
    $$$ indice_dicho(3, [1, 3, 5], compare)
    (True, 1)
    $$$ indice_dicho(4, [1, 3, 5], compare)
    (False, 2)
    $$$ indice_dicho(5, [1, 3, 5], compare)
    (True, 2)
    $$$ indice_dicho(6, [1, 3, 5], compare)
    (False, 3)
    $$$ indice_dicho(42, [], compare)
    (False, 0)
    """
    ...


def inserer(indice: int, elem: C, liste: list[C]) -> NoneType:
    """Insère l'élément elem à l'indice indice de la liste liste.

    Précondition : 0 ≤ indice ≤ len(liste)

    $$$ l = [1, 3, 5]
    $$$ inserer(0, 0, l)
    $$$ l
    [0, 1, 3, 5]
    $$$ inserer(4, 6, l)
    $$$ l
    [0, 1, 3, 5, 6]
    $$$ inserer(3, 4, l)
    $$$ l
    [0, 1, 3, 4, 5, 6]
    $$$ vide = []
    $$$ inserer(0, 42, vide)
    $$$ vide
    [42]
    """
    ...


if __name__ == '__main__':
    import l1test
    l1test.testmod('recherche_dicho.py')

