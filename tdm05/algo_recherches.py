#!/usr/bin/env python3
from typing import Callable
from compare import *

def recherche_seq(elt: A, liste: list[A],
                  a: int = 0, b: int = None,
                  comp: Callable[[A, A], int] = compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
           0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, 20, 2, 11, -1]
    $$$ recherche_seq(-3, l)   # présent en premier
    True
    $$$ recherche_seq(2, l)   # présent au milieu
    True
    $$$ recherche_seq(-1, l)  # présent en dernier
    True
    $$$ recherche_seq(0, l)  # pas présent
    False
    $$$ recherche_seq(0, [])  
    False
    """
    b=len(liste)
    while a<b and comp(elt,liste[a])!=0:
        a+=1
    return a<b

def recherche_seq_rec(elt: A, liste: list[A],
                  a: int = 0, b: int = None,
                  comp: Callable[[A, A], int] = compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
           0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, 20, 2, 11, -1]
    $$$ recherche_seq_rec(-3, l)   # présent en premier
    True
    $$$ recherche_seq_rec(2, l)   # présent au milieu
    True
    $$$ recherche_seq_rec(-1, l)  # présent en dernier
    True
    $$$ recherche_seq_rec(0, l)  # pas présent
    False
    """
    b=len(liste)-len(liste[1:])
    if len(liste)==0:
        return False
    elif len(liste[a:b])==1:
        return comp(elt,liste[0])==0
    else:
        return recherche_seq_rec(elt,liste[1:],a,b,comp) 


def recherche_seq_triee(elt: A, liste: list[A],
                        a:int = 0, b: int = None,
                        comp: Callable[[A, A], int]=compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
            liste est triée selon comp
            0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, -1, 2, 11, 20]  # liste croissante
    $$$ recherche_seq_triee(-3, l)   # présent en premier
    True
    $$$ recherche_seq_triee(2, l)   # présent au milieu
    True
    $$$ recherche_seq_triee(20, l)  # présent en dernier
    True
    $$$ recherche_seq_triee(0, l)  # pas présent
    False
    """
    for entier in liste:
        if comp(elt,)
        

        
        
        


def recherche_seq_triee_rec(elt: A, liste: list[A],
                        a:int = 0, b: int = None,
                        comp: Callable[[A, A], int]=compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
            liste est triée selon comp
            0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, -1, 2, 11, 20]  # liste croissante
    $$$ recherche_seq_triee_rec(-3, l)   # présent en premier
    True
    $$$ recherche_seq_triee_rec(2, l)   # présent au milieu
    True
    $$$ recherche_seq_triee_rec(20, l)  # présent en dernier
    True
    $$$ recherche_seq_triee_rec(0, l)  # pas présent
    False
    """
    ...

def recherche_dicho(elt: A, liste: list[A],
                    a: int = 0, b: int = None,
                    comp: Callable[[A, A], int] = compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
            liste est triée selon comp
            0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, -1, 2, 11, 20]  # liste croissante
    $$$ recherche_dicho(-3, l)   # présent en premier
    True
    $$$ recherche_dicho(2, l)   # présent au milieu
    True
    $$$ recherche_dicho(20, l)  # présent en dernier
    True
    $$$ recherche_dicho(0, l)  # pas présent 
    False
    """
    ...


def recherche_dicho_rec(elt: A, liste: list[A],
                    a: int = 0, b: int = None,
                    comp: Callable[[A, A], int] = compare) -> bool:
    """Renvoie :
      - True si elt est dans liste[a:b] (recherche fructueuse)
      - False sinon (recherche infructueuse)

    Preconditions : les éléments de liste et elt sont comparables à l'aide comp
            liste est triée selon comp
            0 <= a <= b <= len(liste)

    Exemples:
    $$$ l = [-3, -1, 2, 11, 20]  # liste croissante
    $$$ recherche_dicho_rec(-3, l)   # présent en premier
    True
    $$$ recherche_dicho_rec(2, l)   # présent au milieu
    True
    $$$ recherche_dicho_rec(20, l)  # présent en dernier
    True
    $$$ recherche_dicho_rec(0, l)  # pas présent
    False
    """
