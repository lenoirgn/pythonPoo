#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - Faculté des Sciences et Technologies - 
         Univ. Lille <http://portail.fil.univ-lille.fr>_

:date: 2022, march
:last revision: 2026, march

Fournit :
- une classe `ApLst` pour les listes non mutables
- une exception `ApLstError`

Les listes ApLst sont soit vides, soit des objets à deux attributs :
- un attribut `head` représentant la valeur du premier élément de la liste,
- un attribut `tail` représentant le reste de la liste.
"""


class ApLstError(Exception):
    """Les exceptions utilisées par les méthodes de la classe `ApLst`."""

    def __init__(self, msg: str):
        """Initialise une erreur."""
        self.message = msg


class ApLst():
    """Structure de liste récursives.

    Exemple(s) :
    $$$ list = ApLst()
    $$$ list.content
    ()
    $$e liste = ApLst("unparam")
    ApLstError
    $$$ list.is_empty()
    True
    $$e list.head()
    ApLstError
    $$e listerr = ApLst(1, ())
    ApLstError
    $$$ list2 = ApLst(1, list)
    $$$ list2.content
    (1, ApLst())
    $$$ list2.is_empty()
    False
    $$$ list2.head()
    1
    $$$ list2.tail().is_empty()
    True
    $$$ l = ApLst(2, list2)
    $$$ repr(l)
    'ApLst(2, ApLst(1, ApLst()))'
    $$$ str(l)
    '[2, 1]'
    $$$ repr(list2)
    'ApLst(1, ApLst())'
    """

    def __init__(self, tete: "Any" = None, reste: "ApLst" = None):
        """Initialise une nouvelle liste récursive.

        - vide si aucun paramètre n'est donné
        - dont la tête est le premier paramètre, et le reste est le second
        ou lève une erreur si un seul pamètre ou si le 2ème n'est pas une liste récursive
        """
        if tete is None and reste is None:
            self.content = ()
        elif tete is None or reste is None:
            raise ApLstError('bad number of arguments')
        elif isinstance(reste, ApLst):
            self.content = (tete, reste)
        else:
            raise ApLstError('bad type for second argument')

    def is_empty(self) -> bool:
        """Renvoie True si la liste récursive est vide, False sinon."""
        return len(self.content) == 0

    def head(self) -> "Any":
        """Renvoie la valeur de la tête ou lève une erreur si la liste est vide.

        précondition : la liste n'est pas vide.
        """
        if self.is_empty():
            raise ApLstError('head: empty list')
        else:
            return self.content[0]

    def tail(self) -> "ApLst":
        """Renvoie le reste de la liste, ou lève une erreur si la liste est vide.

        précondition : la liste n'est pas vide.
        """
        if self.is_empty():
            raise ApLstError('head: empty list')
        else:
            return self.content[1]

    def __str__(self) -> str:
        """Renvoie la représentation sous forme de chaîne de caractères de la liste récursive.

        précondition : aucune
        """
        def str_content(self, item_number=0):
            if self.is_empty():
                return ''
            elif item_number == 50:
                return ', ...'
            else:
                comma = '' if item_number == 0 else ', '
                return (comma + str(self.head()) +
                        str_content(self.tail(), item_number + 1))
        return f'[{str_content(self)}]'

    def __repr__(self) -> str:
        """Renvoie une représentation textuelle de la liste.

        précondition : aucune
        """
        if self.is_empty():
            content = ""
        else:
            content = f"{repr(self.head())}, {repr(self.tail())}"
        return f"ApLst({content})"

    def __eq__(self, other: "Any") -> bool:
        """Renvoie True si et seulement si les deux listes récursives sont égales.

        c'est-à-dire si leurs représentations sont identiques.

        précondition : aucune.

        Exemple(s) :
        $$$ l1 = ApLst(3, ApLst(1, ApLst(4, ApLst())))
        $$$ l1 == ApLst(3, ApLst(1, ApLst(4, ApLst())))
        True
        $$$ l1 == ApLst()
        False
        $$$ l1 == (3, (1, (4, ())))
        False
        """
        if not isinstance(other, ApLst):
            return False
        return repr(self) == repr(other)
