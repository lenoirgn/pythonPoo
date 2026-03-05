#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`tris` module
:author: FIL - Faculté des Sciences et Technologies -
         Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2015, january
:dernière révision: février 2026

Tris de listes
- tri par sélection
- tri par insertion

"""

from types import NoneType
from typing import Callable, TypeVar
from annexe_tris import *
from genere_listes import genere_lint_croissante
from random import shuffle
T = TypeVar('T')


################################################
#  TRI PAR SELECTION                           #
################################################

def echanger(liste: list[T], i: int, j: int) -> NoneType:
    """ Échange les éléments d'indice i et j de liste.

    Précondition : 0 <= i,j < len(liste)
    Exemple(s) :
    $$$ l1 =  [3, 1, 4, 9, 5, 1, 2]
    $$$ l2 = l1.copy()
    $$$ echanger(l2, 3, 5)
    $$$ (l1[3], l1[5]) == (l2[5], l2[3])
    True
    """
    liste[j],liste[i]=liste[i],liste[j]


def select_min(liste: list[T], a: int, b: int, comp: Callable[[T, T], int]=compare) -> int:
    """ Renvoie l'indice du minimum dans la tranche liste[a:b]

    Précondition : 0 <= a < b <= long(liste),
         éléments de liste comparables avec comp
    Exemple(s):
    $$$ select_min([1, 2, 3, 4, 5, 6, 7, 0], 0, 8)
    7
    $$$ select_min([1, 2, 3, 4, 5, 6, 7, 0], 1, 7)
    1
    $$$ select_min([1, 2, 3, 4, 5, 6, 7, 0], 3, 8)
    7
    """
    imin=a
    for i in range(a+1,b):
        if comp(liste[i],liste[imin])==-1:
            imin=i
    return imin
            


def tri_select(liste: list[T], comp: Callable[[T, T], int] = compare) -> NoneType:
    """ Modifie la liste liste en triant ses éléments selon l'ordre défini par comp
          Algorithme du tri par sélection du minimum
    Précondition : liste liste homogène d'éléments comparables selon comp
    Exemple(s):
    $$$ liste = [3, 1, 4, 1, 5, 9, 2]
    $$$ tri_select(liste)
    $$$ liste == [1, 1, 2, 3, 4, 5, 9]
    True
    """
    for i in range(len(liste)-1):
        imin=i+select_min(liste[i:],0,len(liste[i:]), comp)
        echanger(liste,imin,i)
        

    # à l'issue de l'itération la tranche liste[0:n] est triée

################################################
#  TRI PAR INSERTION                           #
################################################

def inserer(liste: list[T], i: int, comp: Callable[[T, T], int] = compare) -> NoneType:
    """ Insère l'élément liste[i] à sa place dans la tranche liste[0:i+1]
    de sorte que cette tranche soit triée, si liste[0:i] l'est auparavant

    Précondition : 0 <= i < long(liste)
         éléments de liste comparables par comp
         
    Exemple(s) :
    $$$ liste = [1, 2, 4, 5, 3, 7, 6]
    $$$ inserer(liste, 4)
    $$$ liste == [1, 2, 3, 4, 5, 7, 6]
    True
    $$$ inserer(liste, 5)
    $$$ liste == [1, 2, 3, 4, 5, 7, 6]
    True
    $$$ inserer(liste, 6)
    $$$ liste == [1, 2, 3, 4, 5, 6, 7]
    True
    """
    
    for j in range(i,0,-1):
        if comp(liste[j],liste[j-1])==-1:
            echanger(liste,j,j-1)
    

def tri_insert(liste: list[T], comp: Callable[[T, T], int] = compare) -> NoneType:
    """ Modifie la liste liste en triant ses éléments selon l'ordre défini par comp
    Algorithme du tri par insertion
    
    Précondition : liste liste homogène d'éléments comparables selon comp
    Exemple(s) :
    $$$ liste = [3, 1, 4, 1, 5, 9, 2]
    $$$ tri_insert(liste)
    $$$ liste == [1, 1, 2, 3, 4, 5, 9]
    True
    """
    for i in range(len(liste)-1,0,-1):
        inserer(liste,i,comp)
        

    # à l'issue de l'itération la tranche liste[0:n] est triée

