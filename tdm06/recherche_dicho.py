
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
:mod:`recherches` module : un module pour les recherches
:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_
:date: 2026 février
"""
from types import NoneType
from typing import Callable, TypeVar
# On définit un type générique :
C = TypeVar('C')

def compare(x, y):
    return 0 if x == y else 1 if x > y else -1


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
    trouve = False
    debut = 0
    fin = len(liste)-1
    indice = 0
    i = 0
    while i<len(liste) and not trouve :
        if elem>liste[i]:
            indice = i+1
        milieu = (debut+fin)//2
        if comp(liste[i], elem) == 0:
            indice = i
            trouve = True
        elif comp(liste[i], elem) == 1:
            fin = milieu-1
        else:
            debut = milieu+1
        i = i+1
    return (trouve, indice)
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
    liste.append(elem)
    for i in range(len(liste)-1, indice, -1):
        liste[i] = liste[i - 1]
    liste[indice] = elem