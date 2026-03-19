#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`mesures` module : un module pour les mesures de temps

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2026 février

"""
from dicotrie import DicoTrie
from association import Association
from types import NoneType
from timeit import timeit
from random import randrange
import matplotlib.pyplot as plt


def generation_dict(tailles: list[int]) -> list[dict[str, NoneType]]:
    """Renvoie une liste de dictionnaires dont les clés sont les
    représentations des n entiers compris entre 0 et n-1 et les valeurs
    associées None pour chaque entier n dans la liste tailles.

    Précondition : tous les entiers de tailles sont positifs ou nuls

    $$$ generation_dict([0, 2, 4])
    [{}, {'0': None, '1':None}, {'0': None, '1': None, '2': None, '3': None}]
    $$$ generation_dict([0])
    [{}]
    """
    lres=[]
    for elt in tailles:
        dico={}
        for i in range(elt):
            dico[str(i)]=None  
        lres.append(dico)
    return lres
    


def generation_dicotrie(tailles: list[int]) -> list[DicoTrie]:
    """Renvoie une liste de DicoTrie dont les clés sont les représentations
    des n entiers compris entre 0 et n-1 et les valeurs associées None pour
    chaque entier n dans la liste tailles.

    Précondition : tous les entiers de tailles sont positifs ou nuls

    $$$ generation_dicotrie([0, 2])
    [DicoTrie([]), DicoTrie([Association('0', None), Association('1', None)])]
    """
    lres=[]
    for elt in tailles:
        if elt==0:
            lres.append(DicoTrie([]))
        else:
            liste_dico=[]
            for i in range(elt):
                liste_dico.append(Association(str(i),None))   
            lres.append(DicoTrie(liste_dico))
    return lres
 
def mesure_temps_acces(taille : int, d: dict[str, NoneType] | DicoTrie) -> float:
    """Renvoie le temps moyen mis pour accéder à 1000 éléments quelconques
    du dictionnaire d.

    Précondition : les clés de d sont les représentations des entiers
    compris entre 0 et taille - 1.
    """
    cles_a_tester = [str(randrange(taille)) for _ in range(1000)]
    stmt = "all(d[cle] == None for cle in cles_a_tester)"
    return timeit(stmt = stmt, globals = locals(), number = 1) / 1000


def mesures_temps_acces_dict(tailles: list[int]) -> list[float]:
    """Renvoie les listes des temps moyens pour accéder à 1000 éléments quelconques
    de chacun des dictionnaires dont les clés sont les remprésentations des
    n entiers compris entre 1 et n-1 pour chaque entier n dans la liste
    tailles.
    
    Précondition : tous les entiers de tailles sont positifs ou nuls
    """
    liste_dico=generation_dict(tailles)
    liste_moy=[]
    for i in range(len(tailles)):
        liste_moy.append(mesure_temps_acces(tailles[i],liste_dico[i]))
    return liste_moy


def mesures_temps_acces_dicotrie(tailles: list[int]) -> list[float]:
    """Renvoie les listes des temps moyens pour accéder à 1000 éléments quelconques
    de chacun des DicoTrie dont les clés sont les remprésentations des
    n entiers compris entre 1 et n-1 pour chaque entier n dans la liste
    tailles.
    
    Précondition : tous les entiers de tailles sont positifs ou nuls
    """
    liste_dico=generation_dicotrie(tailles)
    liste_moy=[]
    for i in range(len(tailles)):
        liste_moy.append(mesure_temps_acces(tailles[i],liste_dico[i]))
    return liste_moy
#print(mesures_temps_acces_dicotrie([i for i in range(1,100)]))
    

if __name__ == '__main__':

#     import apl1test
#     apl1test.testmod('mesures.py')
    
    lmesure_temps_acces_dict=mesures_temps_acces_dict([1,3,4,6])
    lmesures_temps_acces_dicotrie=mesures_temps_acces_dicotrie([1,3,4,6])
    
    abcisse=[i for i in range(4)]
    plt.plot(abcisse, lmesure_temps_acces_dict, color='blue')
    plt.show()

    #import apl1test
    #apl1test.testmod('mesures.py')
  
    # Écrivez ici le code permettant de faire des hypothèses sur la
    # vitesse d'accès aux dictionnaires.

    # linéaire
     #tailles = list(range(0, 100000,1000))
#      temps_dict = mesures_temps_acces_dict(tailles)
#      temps_dicotrie = mesures_temps_acces_dicotrie(tailles)
#      plt.plot(tailles, temps_dict, '+')
#      plt.plot(tailles, temps_dicotrie, '.')
#      plt.show()
    # log
     tailles = [2**n for n in range(16)]
     temps_dict = mesures_temps_acces_dict(tailles)
     temps_dicotrie = mesures_temps_acces_dicotrie(tailles)
     print(temps_dicotrie)
#      plt.plot(range(16), temps_dict, '+')
#      plt.plot(range(16), temps_dicotrie, '.')
#      plt.show()
#     

