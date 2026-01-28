#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`date` module :  a  module for date

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2026, january. Last revision: 2026, january

Heure are objects

"""

from typing import Any, Self


class Heure:
    def __init__(self, heure: int, minutes: int):
        """Initialise une nouvelle heure.

        Précondition : heure est entre 0 et 23, et minutes entre 0 et 59.

        Exemples :
        $$$ une_heure = Heure(10, 30)
        $$$ type(une_heure) == Heure
        True
        """
        self.heure = heure
        self.minutes = minutes

    def __repr__(self) -> str:
        """Renvoie une représentation non ambiguë de l'objet Heure.

        Exemples :
        $$$ une_heure = Heure(10, 30)
        $$$ repr(une_heure)
        'Heure(10, 30)'
        """
        return f"Heure({self.heure}, {self.minutes})"

    def __str__(self) -> str:
        """Renvoie une chaîne représentant l'heure au format HH:MM.

        
        Exemples :
        $$$ une_heure = Heure(10, 30)
        $$$ str(une_heure)
        '10h30'
        """
        return f"{self.heure:02d}h{self.minutes:02d}"

    def __eq__(self, other: Self) -> bool:
        """Renvoie True si, et seulement si, deux heures sont égales.

        Exemples :
        $$$ h1 = Heure(10, 30)
        $$$ h2 = Heure(10, 30)
        $$$ h1 == h2
        True
        $$$ h3 = Heure(11, 30)
        $$$ h1 == h3
        False
        """
        if not isinstance(other, Heure):
            return False
        return self.heure == other.heure and self.minutes == other.minutes

    def __lt__(self, other: Self) -> bool:
        """Renvoie True si, et seulement si, l'heure actuelle est antérieure à l'autre.

        Exemples :
        $$$ h1 = Heure(10, 30)
        $$$ h2 = Heure(11, 30)
        $$$ h1 < h2
        True
        $$$ h3 = Heure(10, 29)
        $$$ h1 < h3
        False
        """
        return (self.heure, self.minutes) < (other.heure, other.minutes)

    def __le__(self, other: Self) -> bool:
        """Renvoie True si, et seulement si, l'heure actuelle est antérieure ou égale à l'autre.

        Exemples :
        $$$ h1 = Heure(10, 30)
        $$$ h2 = Heure(11, 30)
        $$$ h1 <= h2
        True
        $$$ h3 = Heure(10, 30)
        $$$ h1 <= h3
        True
        """
        return self < other or self == other


if __name__ == '__main__':
    import l1test
    l1test.testmod('heure.py')
