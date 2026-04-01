#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`war` game

:author: `FIL - Faculté des Sciences et Technologies -
         Univ. Lille <http://portail.fil.univ-lille1.fr>`

:date: 2021, april.
:last revision: 2024, march.
"""

from card import Card
from apqueue import *
from apstack import *


def distribute(n_card: int) -> tuple[ApQueue, ApQueue]:
    """
    renvoie un couple (m1, m2) constitué de deux files,
    contenant pour chacune `n_card` cartes

    precondition : n_card > 0
    exemples :

    $$$ m1, m2 = distribute( 4 )
    $$$ len(m1) == 4
    True
    $$$ len(m2) == 4
    True
    $$$ type(m1) == ApQueue
    True
    $$$ type(m2) == ApQueue
    True
    $$$ carte = m1.dequeue()
    $$$ isinstance(carte, Card)
    True
    """
    ...

def gather_stack(main: ApQueue, pile: ApStack) -> None:
    """
    ajoute les carte de la pile dans la main

    exemples :

    $$$ cartes = Card.deck(4)
    $$$ main = ApQueue()
    $$$ pile = ApStack()
    $$$ for c in cartes: pile.push(c)
    $$$ gather_stack( main, pile )
    $$$ len( main ) == 4
    True
    $$$ all( main.dequeue() == cartes[ 3 - i ] for i in range(3))
    True
    """
    ...

def play_one_round(m1: ApQueue, m2: ApQueue, pile: ApStack) -> None:
    """
    Simule une étape du jeu :
    `j1`` et ``j2`` prennent la première carte de leur
    main. On compare les deux cartes :

    * Si la carte de ``j1`` est supérieure à celle de ``j2``, alors
    ``j1`` remporte toutes les cartes de la pile ;
    * Si la carte de ``j1`` est inférieure à celle de ``j2``, alors
    ``j2`` remporte toutes les cartes de la pile ;
    * Si les cartes sont égales, alors elles sont *empilées* sur la
      pile.

    precondition : m1 et m2 ne sont pas vides
    """
    ...

def play(n_card: int, n_round: int) -> None:
    """
    simule une partie de bataille

    n_card: le nombre de cartes à distribuer à chaque joueur.
    n_round: le nombre maximal de tours
    """
    ...


if __name__ == "__main__":
    import l1test
    l1test.testmod("war.py")

