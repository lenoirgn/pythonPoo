#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module 

:author: `FIL - Faculté des Sciences et Technologies - 
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2017, september.
:last revision: mars 26

"""
from __future__ import annotations

import random


class Card:
    """
    Représente une carte définie par une valeur et une couleur.

    Les valeurs possibles sont celles du tuple ``Card.VALUES``.
    Les couleurs possibles sont celles du tuple ``Card.COLORS``.

    $$$ c1 = Card("Ace", "heart")
    $$$ c1.color
    'heart'
    $$$ c1.value
    'Ace'
    $$$ c1
    Card("Ace", "heart")
    $$$ c2 = Card("King", "spade")
    $$$ c2.value in Card.VALUES
    True
    $$$ c2.color in Card.COLORS
    True
    $$$ c1 == c1
    True
    $$$ c1 != c1
    False
    $$$ c1 < c1
    False
    $$$ c1 <= c1
    True
    """

    # tuples des valeurs et couleurs possibles.
    VALUES = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Knight", "Queen", "King")
    COLORS = ("spade", "heart", "diamond", "club")

    def __init__(self, value: str, color: str):
        """Initialise une carte avec une valeur et une couleur données.

        précondition : value in VALUES and color in COLORS
        """
        self.value=value
        self.color=color

    def __hash__(self) -> int:
        """Renvoie un haché de self."""
        return hash((self.color, self.value))

    def __repr__(self) -> str:
        """Renvoie une représentation textuelle de la carte.

        $$$ repr(Card('Ace', 'heart'))
        'Card("Ace", "heart")'
        """
        return f'Card("{(self.value)}", "{self.color}")'

    def __str__(self) -> str:
        """Renvoie une représentation textuelle de la carte.

        $$$ str(Card('Ace', 'heart'))
        'Ace of heart'
        """
        return f'{self.value} of {self.color}'

    def compare(self, card: Card) -> int:
        """Compare deux cartes.

        L'ordre des cartes est celui des valeurs.

        Renvoie :
           * un nombre positif si self est supérieur à card ;
           * un nombre négatif si self est inférieur à card ;
           * 0 si les deux cartes sont de même valeur.

        précondition: none
        exemples :

        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('King', 'heart')
        $$$ c3 = Card('Ace','spade')
        $$$ c1bis = Card('Ace','heart')
        $$$ c1.compare(c2) < 0
        True
        $$$ c2.compare(c1) > 0
        True
        $$$ c1.compare(c3) == 0
        True
        """
        if isinstance(card, Card):
            if self.value > card.value:
                return 1
            elif self.value < card.value:
                return -1
            else:
                return 0
        

    @staticmethod
    def deck(n_card: int) -> list[Card]:
        """Renvoie une liste de n_card cartes choisies au hasard.

        precondition: n_card > 0 and n_card <= 4*13

        Exemples:

        $$$ cartes = Card.deck( 10 )
        $$$ len(cartes) == 10
        True
        $$$ all( isinstance(c, Card) for c in cartes)
        True
        $$$ len(set(cartes))
        len(cartes)
        """
        liste=[]
        for i in range(n_card):
            Value=Card.VALUES[random.randint(0,13)]
            color=Card.COLORS[random.randint(0,3)]
            liste.append(Card(Value, color))
        return liste

    def __eq__(self, card: Card) -> bool:
        """Renvoie True ssi les self et card sont égales."""
        if isinstance(card, Card):
            return self.compare(card)==0

    def __neq__(self, card: Card) -> bool:
        """Renvoie True ssi self et card sont différentes."""
        if isinstance(card, Card):
            return self.compare(card)!=0

    def __lt__(self, card: Card) -> bool:
        """Renvoie True ssi self < card."""
        if isinstance(card, Card):
            return self.compare(card)==-1

    def __le__(self, card: Card) -> bool:
        """Renvoie True ssi self <= card."""
        if isinstance(card, Card):
            return self.compare(card)<=0

    def __gt__(self, card: Card) -> bool:
        """Renvoie True ssi self > card."""
        if isinstance(card, Card):
            return self.compare(card) == 1

    def __ge__(self, card: Card) -> bool:
        """Renvoie True ssi self >= card."""
        if isinstance(card, Card):
            return self.compare(card) >= 0


if __name__ == '__main__':
    import l1test
    l1test.testmod('card.py')

