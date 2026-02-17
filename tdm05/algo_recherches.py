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
    if b is None :
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
    if b is None :
        b=len(liste)-len(liste[1:])
    if len(liste)==0:
        return False
    elif len(liste[a:b])==1:
        if comp(elt,liste[0])==0:
            return True
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
    if b is None :
        b=len(liste)
    for a in range(b):
        c=comp(elt,liste[a])
        if  c==0:
            return True
        if c==-1:
            return False
    return False
     

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
    if b is None :
        b=len(liste)-len(liste[1:])
    if len(liste)==0:
        return False
    elif len(liste[a:b])==1:
        if comp(elt,liste[0])==0:
            return True
        elif comp(elt,liste[0])==-1:
            return False
        else:
            return recherche_seq_rec(elt,liste[1:],a,b,comp) 
    
        
    

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
    if b is None :
        b=len(liste)
    m=b//2
    if comp(elt,liste[m])==1 or comp(elt,liste[m])==0:
        res=recherche_seq_triee(elt, liste[m:],m, len(liste[m:]),comp)
    else:
        res=recherche_seq_triee(elt, liste[:m],a, len(liste[:m]),comp)
    return res
        

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
    if b is None :
        b=len(liste)
    if b==0:
        return False
    elif b==1:
        c=comp(elt,liste[0])
        if c==0:
            return True
        else:
            return False
    else:
        m=b//2
        c=comp(elt,liste[m])
        if c==1 or c==0:
            return recherche_dicho_rec(elt, liste[m:],m, len(liste[m:]),comp)
        else:
            return  recherche_dicho_rec(elt, liste[:m],a, len(liste[:m]),comp)

    
    
