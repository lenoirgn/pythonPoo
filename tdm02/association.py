#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`association` module : un module pour les associations clé-valeur

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2024 février

"""
from ap_decorators import count
from typing import TypeVar

# On définit deux types génériques :
# - C pour le type des clés
# - V pour le type des valeurs

C = TypeVar('C')
V = TypeVar('V')


class Association:
    """Classe d'une association clé-valeur
    """

    def __init__(self, cle: C, valeur: V):
        """
        $$$ asso1 = Association('a', 1)
        $$$ asso1.cle
        'a'
        $$$ asso1.valeur
        1
        """
        self.cle = cle
        self.valeur = valeur

    def __repr__(self) -> str:
        """
        $$$ repr(Association(2, 3))
        'Association(2, 3)'
        $$$ repr(Association('a', 1))
        "Association('a', 1)"
        $$$ repr(Association((1, True), [1, 2, 3]))
        'Association((1, True), [1, 2, 3])'
        $$$ repr(Association(1+1 == 2, "Vrai")) 
        "Association(True, 'Vrai')"
        """


    def __eq__(self, autre) -> bool:
        """
        $$$ Association('a', 1) == Association('a', 1)
        True
        $$$ Association('a', 1) == Association('a', 2)
        False
        $$$ Association('a', 1) == Association(1, 'a')
        False
        $$$ Association('a', 1) == ('a', 1)
        False
        """
        if isinstance(autre, Association)  :
            return self.cle == autre.cle and self.valeur == autre.valeur
        return False


@count
def comp_asso(a1: Association, a2: Association) -> int:
    """Renvoie 0 si les clés de a1 et a2 sont identiques
               -1 si la clé de a1 < la clé de a2
               1 si la clé de a1 > la clé de a2

    Precondition : les clés de a1 et a2 sont comparables

    $$$ comp_asso(Association(1, 'a'), Association(1, 'c'))
    0
    $$$ comp_asso(Association(1, 'a'), Association(2, 'a'))
    -1
    $$$ comp_asso(Association(1, 'd'), Association(0, 'c'))
    1
    """
    if a1.cle == a2.cle:
        return 0
    elif a1.valeur < a2.valeur:
        return -1
    else:
        return 1


if __name__ == '__main__':
    import l1test
    l1test.testmod('association.py')

