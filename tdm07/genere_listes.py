#!/usr/bin/env python3
from typing import Callable
from compare import *


def genere_lint_croissante(n:int)->list[int]:
    """ Génère une liste croissante de n entiers pairs compris entre 0 et 2n

    Précondition : n > 0
    Exemple(s) :
    $$$ genere_lint_croissante(1)
    [0]
    $$$ genere_lint_croissante(10)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    lres=[]
    for i in range(n):
        lres.append(2*i)
    return lres

def genere_lint_decroissante(n:int)->list[int]:
    """ Génère une liste décroissante de n entiers pairs compris entre 2n et 0

    Précondition : n > 0
    Exemple(s) :
    $$$ genere_lint_decroissante(1)
    [0]
    $$$ genere_lint_decroissante(10)
    [18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
    """
    lres=[]
    for i in range(n):
        lres.append(2*i)
    return lres[::-1]
    


def est_triee(liste: list[A], comp: Callable[[A, A], int]=compare) -> bool:
    """ Renvoie True si la liste est triée selon comp et False sinon

    Préconditions : les éléments de liste sont comparables à l'aide de comp
    Exemple(s) :
    $$$ l = list(range(0, 200, 2))  # liste triée de nombres pairs
    $$$ est_triee(l)
    True
    $$$ l[10], l[11] = l[11], l[10] # échange de 2 valeurs au milieu de l
    $$$ est_triee(l)
    False    
    $$$ l = ["liste", "non", "triée", "attention"] # non triée en fin
    $$$ est_triee(l)
    False
    $$$ l = [(10, 1), (-1, 3), (5, 10), (3, 33)] # non triée au début, sur position 0 du tuple
    $$$ est_triee(l)
    False
    $$$ est_triee(l, compare_deuxieme) # mais triée sur 2ème position du tuple
    True
    $$$ est_triee(l)
    False
    """
    i=0
    while i<len(liste)-1 and comp(liste[i],liste[i+1])!=1:
        i+=1
    return i==len(liste)-1
#     trie=True
#     for i in range(len(liste)-1):
#         if comp(liste[i],liste[i+1])==1:
#             trie=False
#     return trie

           
            

def est_triee_rec(liste: list[A], comp: Callable[[A, A], int]=compare) -> bool:
    """ Renvoie True si la liste est triée selon comp et False sinon

    Préconditions : les éléments de liste sont comparables à l'aide de comp
    Exemple(s) :
    $$$ l = list(range(0, 200, 2))  # liste triée de nombres pairs
    $$$ est_triee_rec(l)
    True
    $$$ l[10], l[11] = l[11], l[10] # échange de 2 valeurs au milieu de l
    $$$ est_triee_rec(l)
    False    
    $$$ l = ["liste", "non", "triée", "attention"] # non triée en fin
    $$$ est_triee_rec(l)
    False
    $$$ l = [(10, 1), (-1, 3), (5, 10), (3, 33)] # non triée au début, sur position 0 du tuple
    $$$ est_triee_rec(l)
    False
    $$$ est_triee_rec(l, compare_deuxieme) # mais triée sur 2ème position du tuple
    True
    $$$ est_triee_rec(l)
    False
    """
    if len(liste)==0 or len(liste)==1:
        return True
    elif comp(liste[0],liste[1])!=1:
        return est_triee_rec(liste[1:],comp)
    else:
        return False
    
    
    
    

if __name__ == '__main__':
    liste_cro=genere_lint_croissante(20)
    liste_decro=genere_lint_decroissante(20)
    print(est_triee(liste_cro,compare))
    #True
    print(est_triee(liste_decro,not_compare))
    #True