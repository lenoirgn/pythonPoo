#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`dicotrie` module : un module pour les ensembles d'associations

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2024 février

"""

from association import Association, C, V, comp_asso
from recherches import indice_dicho, inserer
from types import NoneType


class DicoTrie:
    """Classe d'une association clé-valeur
    """

    def __init__(self, liste_assos: list[Association]):
        """
        """
        ...

    def __repr__(self) -> str:
        """
        $$$ repr(DicoTrie([Association('a', 1)]))
        "DicoTrie([Association('a', 1)])"
        $$$ repr(DicoTrie([Association('a', 1), Association('b', 2)]))
        "DicoTrie([Association('a', 1), Association('b', 2)])"
        $$$ repr(DicoTrie([Association('c', 3), Association('a', 2), Association('b', 1)]))
        "DicoTrie([Association('a', 2), Association('b', 1), Association('c', 3)])"
        """
        ...

    def __eq__(self, autre) -> bool:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d2 = DicoTrie([Association("b", 2), Association("a", 1)])
        $$$ d3 = DicoTrie([Association("a", 1), Association("b", 2), Association("c", 3)])
        $$$ d1 == d2
        True
        $$$ d1 == d3
        False
        $$$ d1 == {"a": 1, "b": 2}
        False
        """
        ...

    def __setitem__(self, cle: C, valeur: V) -> NoneType:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d1["c"] = 3
        $$$ d1
        DicoTrie([Association("a", 1), Association("b", 2), Association("c", 3)])
        """
        ...

    def __getitem__(self, cle: C) -> V:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d1['a']
        1
        $$$ d1['b']
        2
        $$e d1['c']
        KeyError
        """
        ...

    def __delitem__(self, cle: C) -> NoneType:
        """ 
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)]) 
        $$$ del d1['a'] 
        $$$ d1 
        DicoTrie([Association("b", 2)]) 
        $$e del d1['c'] 
        KeyError 
        """
        ...

    def __contains__(self, cle: C) -> bool:
        """ 
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)]) 
        $$$ 'a' in d1
        True
        $$$ 'c' in d1
        False
        """
        ...


if __name__ == '__main__':
    import apl1test
    apl1test.testmod('dicotrie.py')

