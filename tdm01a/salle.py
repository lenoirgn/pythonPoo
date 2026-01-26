#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2026
:Fournit :
"""


class Salle:
    """Une classe représentant une salle."""

    def __init__(self, nom: str, batiment: str):
        """Initialise une nouvelle salle.

        précondition: nom et batiment ne sont pas vides.

        exemples :

        $$$ s = Salle('a5', 'm5')
        $$$ s.nom
        'a5'
        $$$ s.batiment
        'm5'
        """
        self.nom = nom
        self.batiment = batiment
        assert self.nom != '' and self.batiment != '', "Invalid"

    def __eq__(self, other):
        """Renvoie True ssi other est une salle de même nom et de même bâtiment.

        précondition: \

        exemples :

        $$$ Salle('a5', 'sup') == 'a5'
        False
        $$$ Salle('a5', 'sup') == Salle('a5', 'm5')
        False
        $$$ Salle('a5', 'm5') == Salle('a5', 'm5')
        True
        """
        if isinstance(other, Salle) and isinstance(self, Salle) :
            if self.nom == other.nom and self.batiment == other.batiment:
                return True
        return False


if __name__ == '__main__':
    import l1test
    l1test.testmod('salle.py')

