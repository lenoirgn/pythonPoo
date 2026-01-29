#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2026
:Fournit :
"""
from typing import Self

from date import Date
from salle import Salle
from ue import Ue
from heure import Heure


class Creneau:
    """Une classe représentant un créneau."""

    def __init__(self, date: Date, debut: int, fin: int,
                 ue: Ue, salle: Salle):
        """Initialise un nouveau crénau.

        précondition: \

        exemples :

        $$$ c = Creneau(Date(12,1,26), Heure(8, 30), Heure(10, 00), Ue('ap', 'MI'), Salle('maxwell', 'p3'))
        $$$ c.date
        Date(12, 1, 26)
        $$$ c.debut
        Heure(8, 30)
        $$$ c.fin
        Heure(10, 0)
        $$$ c.ue
        Ue('ap', 'MI')
        $$$ c.salle
        Salle('maxwell', 'p3')
        """
        self.date = date
        self.debut = debut
        self.fin = fin
        self.ue = ue
        self.salle = salle

    def __lt__(self, other: Self):
        """Renvoie True ssi self commence avant other."""
        if isinstance(self, Creneau) and isinstance(other, Creneau):
            if self.date <= other.date and self.debut < other.debut :
                return True
        return False





if __name__ == '__main__':
    import l1test
    l1test.testmod('creneau.py')

