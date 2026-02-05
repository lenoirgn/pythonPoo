#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Noms : Sow
# Prenoms : Mamadou Radjaye
# Groupe : MI23
# Date : 05/02/2026



"""

:mod: module `recursivite`
:author: FIL - Faculté des Sciences et Technologies - Univ. Lille
:link: <http://portail.fil.univ-lille1.fr>_
:date: Mars 2020
:dernière révision: janvier 2024

"""

from ap_decorators import count, trace
# l'instruction suivante permet d'annoter des paramètres qui sont des functions.
from collections.abc import Callable


def taille_binaire(naturel: int) -> int:
    """
    Renvoie le nombre de chiffres dans l'écriture binaire de l'entier naturel `naturel`

    Précondition :
       naturel >= 0

    Exemples :
    $$$ taille_binaire(0)
    1
    $$$ taille_binaire(1)
    1
    $$$ taille_binaire(2)
    2
    $$$ taille_binaire(1023)
    10
    $$$ taille_binaire(1024)
    11
    $$$ from random import randrange
    $$$ l = [randrange(1,2**100)  for _ in range(100)]
    $$$ all(taille_binaire(elt) == len(bin(elt))-2  for elt in l)
    True

    """
    res = 1
    while naturel >= 2:
        res += 1
        naturel //= 2
    return res

def taille_binaire_recursive(naturel: int) -> int:
    """
    Renvoie le nombre de chiffres dans l'écriture binaire de l'entier naturel `naturel`

    Précondition :
       naturel >= 0

    Exemples :
    $$$ taille_binaire_recursive(0)
    1
    $$$ taille_binaire_recursive(1)
    1
    $$$ taille_binaire_recursive(2)
    2
    $$$ taille_binaire_recursive(1023)
    10
    $$$ taille_binaire_recursive(1024)
    11
    $$$ from random import randrange
    $$$ l = [randrange(1,2**100)  for _ in range(100)]
    $$$ all(taille_binaire_recursive(elt) == len(bin(elt))-2  for elt in l)
    True
    """
    if naturel<2:
        return 1
    else:
        return 1+taille_binaire(naturel//2)

def poids_binaire(naturel: int) -> int:
    """
    Renvoie le nombre de chiffre 1 dans l'écriture binaire de l'entier naturel `naturel`

    Précondition :
       naturel >= 0

    Exxemples :

    $$$ poids_binaire(0)
    0
    $$$ poids_binaire(1)
    1
    $$$ poids_binaire(2)
    1
    $$$ poids_binaire(255)
    8
    $$$ from random import randrange
    $$$ l = [randrange(1,2**100)  for _ in range(100)]
    $$$ all([poids_binaire(x)==bin(x).count('1') for x in l])
    True
    """
    res = naturel % 2
    while naturel > 0:
        naturel //= 2
        res += naturel % 2
    return res


def poids_binaire_recursif(naturel: int) -> int:
    """
    Renvoie le nombre de chiffre 1 dans l'écriture binaire de l'entier naturel `naturel`

    Précondition :
       naturel >= 0

    Exxemples :

    $$$ poids_binaire_recursif(0)
    0
    $$$ poids_binaire_recursif(1)
    1
    $$$ poids_binaire_recursif(2)
    1
    $$$ poids_binaire_recursif(255)
    8
    $$$ from random import randrange
    $$$ l = [randrange(1, 2**100)  for _ in range(100)]
    $$$ all([poids_binaire_recursif(x)==bin(x).count('1') for x in l])
    True
    """
    if naturel==0:
        return 0
    return (naturel%2) +poids_binaire_recursif(naturel//2)
        
print(poids_binaire_recursif(17))   

def puissance(x: int|float, n: int) -> int|float:
    """
    Calcule x élevé à la puissance n

    Précondition :
        n>=0

    Exemples :

    $$$ puissance(10, 0)
    1
    $$$ puissance(10, 1)
    10
    $$$ puissance(2, 10)
    1024
    """
    ...

def puissance_v2(x: int|float, n: int) -> int|float:
    """
    calcule  x élevé à la puissance n

    Précondition :   n>=0

    Exemples :
    $$$ puissance_v2(10,0)
    1
    $$$ puissance_v2(10,1)
    10
    $$$ puissance_v2(2,10)
    1024
    """
    ...

@count
def fois(x: int|float, y: int|float) -> int|float:
    """
    renvoie le produit de x par y

    Précondition : les mêmes que l'opérateur *

    Exemples :
    $$$ fois(8, 7)
    56
    """
    return x * y

def comptage(puissance: Callable[[int|float, int], int|float]) -> list[int]:
    """
    Renvoie une liste de longueur 100 contenant le nombre de multiplications
    effectuées par la fonction ``puissance`` passée en paramètre

    Précondition :
       la fonction doit être implantée en utilisant la fonction ``fois``
    """
    res = []
    for i in range(100):
        fois.counter = 0
        _ = puissance(2, i)
        res.append(fois.counter)
    return res

#@trace
def puissance_calbuth(x: int|float, n: int) -> int|float:
    """
    calcule  x élevé à la puissance n

    Précondition :
        n>=0

    Exemples :

    $$$ puissance_calbuth(10,0)
    1
    $$$ puissance_calbuth(10,1)
    10
    $$$ puissance_calbuth(2,10)
    1024

    """
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        k = n // 2
        return puissance_calbuth(x, k) * puissance_calbuth(x, n - k)

def puissance_calbuth_v2(x: int|float, n: int) -> int|float:
    """
    calcule  x élevé à la puissance n

    Précondition :
        n>=0

    Exemples :

    $$$ puissance_calbuth_v2(10,0)
    1
    $$$ puissance_calbuth_v2(10,1)
    10
    $$$ puissance_calbuth_v2(2,10)
    1024

    """
    ...


def puissance_calbuth_v2_amelioree(x: int|float, n: int) -> int|float:
    """
    calcule  x élevé à la puissance n

    Précondition :
        n>=0

    Exemples :

    $$$ puissance_calbuth_v2_amelioree(10,0)
    1
    $$$ puissance_calbuth_v2_amelioree(10,1)
    10
    $$$ puissance_calbuth_v2_amelioree(2,10)
    1024

    """
    ...

def puissance_erronee(x: int|float, n: int) -> int|float:
    """
    aurait dû calculer  x élevé à la puissance n

    Précondition :
       n >= 0

    Exemples :

    $$$ puissance_erronee(10, 0)
    1
    $$$ puissance_erronee(10, 1)
    10
    $$$ #$$$ puissance_erronee(2, 10)
    $$$ #1024
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        r = n % 2
        q = n // 2
        return puissance_erronee(x, r) * puissance_erronee(puissance_erronee(x, q), 2)

def puissance_reparee(x: int|float, n: int) -> int|float:
    """
    calcule  x élevé à la puissance n

    Précondition :
        n>=0

    Exemples :

    $$$ puissance_reparee(10,0)
    1
    $$$ puissance_reparee(10,1)
    10
    $$$ puissance_reparee(2,10)
    1024
    """
    ...

