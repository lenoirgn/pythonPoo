#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2026
:Fournit :
"""

class Ue:
    """Une classe représentant une unité d'enseignement.

    $$$ ap1 = Ue('ap', 'MI')
    $$$ ap1.nom
    'ap'
    $$$ ap1.formation
    'MI'
    """

    def __init__(self, nom: str, formation: str):
        """Initialise une ue.

        précondition: nom != ''
        """
        self.nom = nom
        self.formation = formation
        assert self.nom != '', "nom invalide"

    def __eq__(self, other: object) -> bool:
        """Renvoie True ssi other est une Ue de même nom et
        de même formation que self.

        précondition: \

        exemples :

        $$$ Ue('ap', 'MI') == Ue('tw', 'MI')
        False
        $$$ Ue('ap', 'MI') == "ap"
        False
        $$$ Ue('ap', 'MI') == Ue('ap', 'MI')
        True
        """
        if isinstance(other, Ue) and isinstance(self,Ue) :
            if self.nom == other.nom and self.formation == other.formation:
                return True
        return False



if __name__ == '__main__':
    import l1test
    l1test.testmod('ue.py')

