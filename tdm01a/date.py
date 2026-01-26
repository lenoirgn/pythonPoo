#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`date` module :  a  module for date

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2024, january. Last revision: 2026, january

Date are objects

"""

from typing import Any, Self


NOM_MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
            'août', 'septembre', 'octobre', 'novembre', 'décembre']
DUREE_MOIS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def est_bissextile(annee: int) -> bool:
    """
    Renvoie True si et seulement si annee est bissextile.

    précondition: annee >= 1582.

    $$$ est_bissextile(2024)
    True
    $$$ est_bissextile(2000)
    True
    $$$ est_bissextile(2100)
    False
    """
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


def nombre_de_jour_dans_mois(mois: int, annee: int) -> int:
    """
    Renvoie le nombre de jour dans le mois `mois` de l'année `année`.

    précondition : 0 <= mois < 12 et annee >= 1582.
    """
    duree_mois = DUREE_MOIS[mois - 1]
    if est_bissextile(annee) and mois == 2:
        return duree_mois + 1
    return duree_mois


def nom_mois(mois) -> str:
    """Renvoie le nom du mois en français."""
    return NOM_MOIS[mois - 1]


class Date:
    """Une classe permettant de représenter des dates."""

    def __init__(self, jour: int, mois: int, annee: int):
        """Initialise une nouvelle date.

        précondition : jour/mois/annee est une date valide

        exemples :

        $$$ adate = Date(4, 6, 2024)
        $$$ type(adate) == Date
        True
        """
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self) -> str:
        """Renvoie une chaîne représentant la date.

        $$$ adate = Date(23, 1, 2024)
        $$$ str(adate)
        '23 janvier 2024'
        """
        return f"{self.jour} {nom_mois(self.mois)} {self.annee}"

    def __repr__(self) -> str:
        """Renvoie une représentation textuelle d'une date."""
        return f"Date({self.jour}, {self.mois}, {self.annee})"

    def __eq__(self, other: Any) -> bool:
        """Renvoie True si, et seulement si, deux dates sont égales.

        exemples :

        $$$ adate1 = Date(23, 1, 2024)
        $$$ adate2 = Date(23, 1, 2024)
        $$$ id(adate1) == id(adate2)
        False
        $$$ adate1 == adate2
        True
        """
        if not isinstance(other, Date):
            return False
        return self.jour == other.jour and \
            self.mois == other.mois and \
            self.annee == other.annee

    def __lt__(self, other: Self) -> bool:
        """Compare deux dates.

        Renvoie True si, et seulement si, la date représentée par
        self est avant celle représentée par other.

        précondition: \

        exemples :

        $$$ adate1 = Date(23, 1, 2024)
        $$$ adate2 = Date(25, 1, 2024)
        $$$ adate1 < adate2
        True
        $$$ adate2 < adate1
        False
        $$$ adate1 < Date(23, 1, 2024)
        False
        """
        if self.annee == other.annee:
            if self.mois == other.mois:
                res = self.jour < other.jour
            else:
                res = self.mois < other.mois
        else:
            res = self.annee < other.annee
        return res

    def __le__(self, other: Self) -> bool:
        """Compare deux dates.

        Renvoie True si, et seulement si, la date représentée par
        self est avant ou egale à celle représentée par other.

        précondition: \

        exemples :

        $$$ adate1 = Date(23, 1, 2024)
        $$$ adate2 = Date(25, 1, 2024)
        $$$ adate1 <= adate2
        True
        $$$ adate2 <= adate1
        False
        $$$ adate1 <= Date(23, 1, 2024)
        True
        """
        return self < other or self == other

    def __gt__(self, other: Self) -> bool:
        """Compare deux dates.

        Renvoie True si, et seulement si, la date représentée par
        self est après celle représentée par other.

        précondition: \

        exemples :

        $$$ adate1 = Date(23, 1, 2024)
        $$$ adate2 = Date(25, 1, 2024)
        $$$ adate1 > adate2
        False
        $$$ adate2 > adate1
        True
        $$$ adate1 > Date(23, 1, 2024)
        False
        """
        return not (self <= other)

    def tomorrow(self) -> Self:
        """Renvoie la date du lendemain.

        précondition : \
        $$$ Date(31, 12, 2023).tomorrow() == Date(1, 1, 2024)
        True
        $$$ Date(31, 1, 2024).tomorrow() == Date(1, 2, 2024)
        True
        $$$ Date(24, 1, 2024).tomorrow() == Date(25, 1, 2024)
        True
        """
        annee = self.annee
        mois = self.mois
        jour = self.jour

        if jour == nombre_de_jour_dans_mois(mois, annee):
            jour = 1
            if mois == 12:
                annee = annee + 1
                mois = 1
            else:
                mois = mois + 1
        else:
            jour = jour + 1
        return Date(jour, mois, annee)

    def __add__(self, njour: int) -> Self:
        """Ajoute un nombre de jour à une date.

        précondition: njour >= 0

        $$$ Date(31, 1, 24) + 7
        Date(7, 2, 24)
        """
        res = self
        for _ in range(njour):
            res = res.tomorrow()
        return res

    def __sub__(self, other: Self) -> int:
        """Renvoie le nombre de jour entre deux dates.

        précondition: \

        $$$ Date(7, 2, 24) - Date(31, 1, 24)
        7
        """
        if self <= other:
            start, ending = self, other
        else:
            start, ending = other, self
        res = 0
        while start != ending:
            start = start.tomorrow()
            res = res + 1
        return res


if __name__ == '__main__':
    import l1test
    l1test.testmod('date.py')
