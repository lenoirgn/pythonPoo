#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`dicotable` module : un module pour les dictionnaires.

Le dictionnaire est enregistré dans un tableau d'associations.

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2026 janvier

"""

from typing import Any, Callable

from association import Association, C, V
from table import FANTOME, est_cellule_vide, table_indice, nombre_de_cellules_non_vides

MAX_RATE = 0.6


class DicoTable:
    """Classe d'une association clé-valeur."""

    def __init__(self, n: int = 10):
        """Initialise un dictionnaire avec une table.

        précondition: n > 0

        Exemples:

        $$$ d = DicoTable(20)
        $$$ d.table
        [None] * 20
        $$$ d = DicoTable()
        $$$ d.table
        [None] * 10
        """
        ...

    def __eq__(self, autre) -> bool:
        """Renvoie True ssi les dictionnaires sont égaux.

        Deux dictionnaires sont égaux si ils possèdent les mêmes clés et que les
        éléments qui correspondent à ces clés sont tous égaux.

        Précondition : \

        Exemples :
        
        $$$ d1 = DicoTable() ; d1["a"] = 1; d1["b"] = 2
        $$$ d2 = DicoTable() ; d2["b"] = 2; d2["a"] = 1
        $$$ d3 = DicoTable() ; d3["b"] = 2; d3["a"] = 1 ; d3["c"] = 3
        $$$ d1 == d2
        True
        $$$ d1 == d3
        False
        """
        ...


    def __setitem__(self, cle: C, valeur: V) -> NoneType:
        """Associe la valeur `valeur` à la clé `cle`.

        Si la clé est déjà dans la table, alors modifie l'association.
        Sinon ajoute une nouvelle association.

        précondition : la clé est dans la table ou la table n'est pas pleine.
        
        $$$ d1 = DicoTable()
        $$$ d1["d"] = 4
        $$$ Association("d", 4) in d1.table
        True
        $$$ d1["d"] = 3
        $$$ Association("d", 3) in d1.table
        True
        $$$ Association("d", 4) in d1.table
        False
        """
        ...

    def __len__(self) -> int:
        """Renvoie le nombre d'associations contenues dans le dictionnaire.

        Précondition : \

        Exemples :

        $$$ d = DicoTable()
        $$$ d["a"] = 1
        $$$ d["b"] = 2
        $$$ d["c"] = 3
        $$$ len(d)
        3
        """
        ...

    def taux_de_remplissage(self):
        """Renvoie le taux de remplissage de la table.

        Le taux est le nombre d'association divisé par la taille de la table.
        """
        ...

    def __getitem__(self, cle: C) -> V:
        """Obtient la valeur associée à la clé C.

        Déclenche l'erreur `KeyError` si aucune valeur est associée à `cle`.

        $$$ d1 = DicoTable(); d1["a"] = 1; d1["b"] = 2
        $$$ d1['a']
        1
        $$$ d1['b']
        2
        $$e d1['c']
        KeyError
        """
        ...

    def __delitem__(self, cle: C) -> NoneType:
        """Supprime l'association dans le dictionnaire.

        Si aucune valeur est associée à `cle`, alors déclenche l'erreur `KeyError` 
        sinon remplis la cellule correspondante avec FANTOME.

        $$$ d1 = DicoTable(); d1["a"] = 1; d1["b"] = 2
        $$$ del d1['a']
        $$$ len(d1)
        1
        $$$ d1["b"]
        2
        $$e del d1['c']
        KeyError
        """
        ...

    def __contains__(self, cle: C) -> bool:
        """Renvoie True ssi le dictionnaire contient une association pour `cle`.

        
        $$$ d1 = DicoTable(); d1["a"] = 1; d1["b"] = 2
        $$$ 'a' in d1
        True
        $$$ 'c' in d1
        False
        """
        ...

    def redimensionne(self, nouvelle_taille: int):
        """Redimensionne la table.

        Crée un nouveau dictionnaire de taille `nouvelle_taille`, puis
        recopie les associations. Ensuite associe à self.table la table
        du nouveau dicionnaire.

        Précondition: nouvelle_taille >= len(self)

        $$$ d = DicoTable() ; d["a"] = 1; d["b"] = 2; d["c"] = 3
        $$$ d.redimensionne(20)
        $$$ len(d.table)
        20
        $$$ len(d)
        3
        $$$ all(c in d for c in "abc")
        True
        """
        ...


if __name__ == '__main__':
    import l1test
    l1test.testmod('dicotable.py')

