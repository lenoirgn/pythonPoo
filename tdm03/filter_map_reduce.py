#!/usr/bin/env python3
from typing import Callable


def est_pair(x: int) -> bool:
    """Renvoie True ssi x est pair.

    précondition: \
    """
    return x % 2 == 0


def est_positif(x: int) -> bool:
    """Renvoie True ssi x est positif.

    Précondition : \
    """
    return x >= 0


def carre(x: int) -> int:
    """Renvoie le carré de x.

    Précondition : \
    """
    return x**2


def triple(x: int) -> int:
    """Renvoie le triple de x.

    Précondition : \
    """
    return 3 * x


def somme(x: int, y: int) -> int:
    """Renvoie la somme de x et y.

    Précondition : \
    """
    return x+y


def mini(x: int, y: int) -> int:
    """Renvoie le minimum de x et y.

    Précondition : \
    """
    if x < y:
        return x
    else:
        return y


def liste_filtre(liste: list[int],
                 filtre: Callable[[int], bool]) -> list[int]:
    """Renvoie la liste des éléments x pour lesquels filtre(x) vaut True.

    précondition: \

    Exemple:

    $$$ liste_filtre([3, 7, 2, 0, 15, 42], est_pair)
    [2, 0, 42]
    $$$ liste_filtre([], est_pair)
    []
    $$$ liste_filtre([-3, 1, -4, 1, -5, 9], est_positif)
    [1, 1, 9]
    """
    lres=[]
    for entier in liste:
        if filtre(entier):
            lres.append(entier)
    return lres


def liste_applique(liste: list[int],
                   f: Callable[[int], int]) -> list[int]:
    """Applique la fonction `f` aux éléments de la liste.

    prcondition: \

    Exemples:

    $$$ liste_applique([3, 1, 4, 1, 5], carre)
    [9, 1, 16, 1, 25]
    $$$ liste_applique([], triple)
    []
    """
    lres=[]
    for entier in liste:
        lres.append(f(entier))
    return lres


def liste_reduit(liste: list[int],
                 reduction: Callable[[int, int], int]) -> int:
    """Réduit la liste avec la fonction `reduction`.

    Précondition: liste != []
    Exemples:
    $$$ liste_reduit([1], lambda x, y: x+y)
    1
    $$$ liste_reduit([3, 1, 4, 1, 5, 9, 2, 6], somme)
    3+1+4+1+5+9+2+6
    $$$ liste_reduit([3, 1, 4, 1, 5, 9, 2, 6], mini)
    1
    """
    
    prec=liste[0]
    for entier in liste[1:]:
        prec=reduction(prec,entier)
    return prec
        
        
        


if __name__ == '__main__':
    import l1test
    l1test.testmod('filter_map_reduce.py')

