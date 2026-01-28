#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`dico` module : un module pour les ensembles d'associations

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2026 janvier

"""

from types import NoneType

from association import Association, C, V


class Dico:
    """Classe d'une association clé-valeur."""

    def __init__(self, liste_assos: list[Association]):
        """Initialise un dictionnaire."""
        self.liste_assos = liste_assos


    def indice(self, cle: C) -> tuple[bool, int]:
        """Renvoie le couple (trouve, indice) d'une association de clé `cle`.

        Lorsqu'une telle association existe dans la liste, `trouve` vaut True et indice
        est l'indice de l'association. Sinon `trouve` vaut False et la valeur d'indice
        est quelconque.

        Précondition : \

        Exemples :

        $$$ d = Dico([Association('a', 1), Association('b', 3)])
        $$$ d.indice('a')
        (True, 0)
        $$$ d.indice('b')
        (True, 1)
        $$$ trouve, _ = d.indice('c')
        $$$ trouve
        False
        """
        for i in range(len(self.liste_assos)):
            if self.liste_assos[i].cle == cle:
                trouve = True
            return (trouve, i)
        return (False, 0)

    def __repr__(self) -> str:
        """Renvoie une représentation d'un dictionnaire.

        Exemples :
        $$$ repr(Dico([Association('a', 1)]))
        "Dico([Association('a', 1)])"
        $$$ repr(Dico([Association('c', 3), Association('a', 2), Association('b', 1)]))
        "Dico([Association('c', 3), Association('a', 2), Association('b', 1)])"
        """
        return f"Dico({self.liste_assos})"

    def __eq__(self, autre) -> bool:
        """Renvoie True ssi les dictionnaires sont égaux.

        Deux dictionnaires sont égaux si ils possèdent les mêmes clés et que les
        éléments qui correspondent à ces clés sont tous égaux.

        $$$ d1 = Dico([Association("a", 1), Association("b", 2)])
        $$$ d2 = Dico([Association("b", 2), Association("a", 1)])
        $$$ d3 = Dico([Association("a", 1), Association("b", 2), Association("c", 3)])
        $$$ d1 == d2
        True
        $$$ d1 == d3
        False
        """
        if len(self.liste_assos) == len(autre.liste_assos):
            for asso in autre.liste_assos:
                if asso in self.liste_assos:
                    return True
        return False


    def __setitem__(self, cle: C, valeur: V) -> NoneType:
        """Associe la valeur `valeur` à la clé `cle`.

        $$$ d1 = Dico([Association("a", 1), Association("b", 2)])
        $$$ d1["d"] = 4
        $$$ d1
        Dico([Association("a", 1), Association("b", 2), Association("d", 4)])
        $$$ d1["c"] = 3
        $$$ d1
        Dico([Association("a", 1), Association("b", 2), Association("d", 4), Association("c", 3)])
        """
        elem=Association(cle, valeur)
        Dico.append(elem)
        return Dico


    def __getitem__(self, cle: C) -> V:
        """Obtient la valeur associée à la clé C.

        Déclenche l'erreur `KeyError` si aucune valeur est associée à `cle`.

        $$$ d1 = Dico([Association("a", 1), Association("b", 2)])
        $$$ d1['a']
        1
        $$$ d1['b']
        2
        $$e d1['c']
        KeyError
        """
        for asso in self.liste_assos:
            if asso.cle == cle:
                return asso.valeur
        raise KeyError





    def __delitem__(self, cle: C) -> NoneType:
        """Supprime l'association dans le dictionnaire.

        Déclenche l'erreur `KeyError` si aucune valeur est associée à `cle`.
        
        $$$ d1 = Dico([Association("a", 1), Association("b", 2)])
        $$$ del d1['a']
        $$$ d1
        Dico([Association("b", 2)])
        $$e del d1['c']
        KeyError
        """
        supprime=False
        for i in range(len(self.liste_assos)):
            if self.liste_assos[i].cle == cle:
                self.liste_assos.pop(i)
                supprime=True
                break
        if not  supprime:
            raise KeyError

    def __contains__(self, cle: C) -> bool:
        """Renvoie True ssi le dictionnaire contient une association pour `cle`.

        $$$ d1 = Dico([Association("a", 1), Association("b", 2)])
        $$$ 'a' in d1
        True
        $$$ 'c' in d1
        False
        """
        for asso in self.liste_assos:
            if cle == asso.cle:
                return True
        return False



if __name__ == '__main__':
    import l1test
    l1test.testmod('dico.py')

