from typing import TypeVar
from collections.abc import Callable
from aplst import ApLst

A = TypeVar("A")

def somme(nombres: ApLst) -> int:
    """Renvoie la somme des éléments de `liste`
    Précondition : les éléments de `liste` sont tous entiers
    Exemples :
    $$$ somme(ApLst())
    0
    $$$ somme(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    8
    """
    temp=nombres
    som=0
    while not temp.is_empty():
        som+=temp.head()
        temp=temp.tail()
    return som
        

def sont_tous_pairs(nombres: ApLst) -> bool:
    """Renvoie `True` si toutes les cellules de `nombres` sont paires,
    et False sinon
    Précondition : les éléments de `liste` sont tous entiers
    Exemples :
    $$$ sont_tous_pairs(ApLst())
    True
    $$$ sont_tous_pairs(ApLst(4, ApLst(0, ApLst(4, ApLst()))))
    True
    $$$ sont_tous_pairs(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    False
    $$$ sont_tous_pairs(ApLst(0, ApLst(1, ApLst(2, ApLst()))))
    False
    """
    temp=nombres
    trouve=True
    while not temp.is_empty() and trouve :
        if not temp.head()%2==0:
            trouve=False
        temp=temp.tail()   
    return trouve
    

def appartient(element: A, liste: ApLst) -> bool:
    """Renvoie `True` si une cellule de `liste` contient `element`
    et `False` sinon
    Précondition : aucune
    Exemples:
    $$$ appartient(3, ApLst())
    False
    $$$ appartient(3, ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    True
    $$$ appartient(3, ApLst(1, ApLst(2, ApLst(3, ApLst()))))
    True
    $$$ appartient(3, ApLst(4, ApLst(0, ApLst(4, ApLst()))))
    False
    """
    temp=liste
    
    trouve=False 
    while not temp.is_empty() and not trouve :
        if  temp.head()==element:
            trouve=True 
        temp=temp.tail()   
    return trouve
    

def repetition(a_repeter: A, nb_repetitions: int) -> ApLst:
    """Renvoie une liste de `nb_repetitions` cellules, chacune contenant
    `a_repeter`
    Précondition : nb_repetitions >= 0
    Exemples :
    $$$ repetition("a", 0)
    ApLst()
    $$$ repetition("la", 3)
    ApLst('la', ApLst('la', ApLst('la', ApLst())))
    """
    res=ApLst()
    for i in range(nb_repetitions):
        res=ApLst(a_repeter,res)
    return res
        

def double(nombres: ApLst) -> ApLst:
    """Renvoie la liste dont les cellules contiennent le double de celles
    de `nombres`
    Précondition : aucune
    Exemples
    $$$ double(ApLst())
    ApLst()
    $$$ double(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    ApLst(6, ApLst(2, ApLst(8, ApLst())))
    """
    res=ApLst()
    temp=nombres
    while not temp.is_empty():
        res=ApLst(temp.head()*2,res)
        temp=temp.tail() 
    return res

def que_les_pairs(nombres: ApLst) -> ApLst:
    """Renvoie la liste des éléments pairs de `nombres`
    Précondition : aucune
    $$$ que_les_pairs(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    ApLst(4, ApLst())
    """
    ...

def minimum(liste: ApLst) -> A:
    """Renvoie le plus petit élément de `liste`
    Précondition : `liste` n'est pas vide
    $$$ minimum(ApLst(3, ApLst(1, ApLst(4, ApLst()))))
    1
    """
    ...

def pour_tous(liste: ApLst, p: Callable[[A], bool]) -> bool:
    """Renvoie `True` si tous éléments de `liste` vérifient le prédicat `p`
    et `False` sinon.
    Précondition : chacun des éléments de `liste` vérifie la
                   précondition de `p`
    $$$ def est_superieur_a_2(n: int) -> bool: return n > 2
    $$$ pour_tous(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_superieur_a_2)
    False
    $$$ def est_positif(n: int) -> bool: return n >= 0
    $$$ pour_tous(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_positif)
    True
    $$$ def est_une_licorne(x): return False # les licornes n'existent pas :'(
    $$$ pour_tous(ApLst(), est_une_licorne)
    True
    """
    ...

def il_existe(liste: ApLst, p: Callable[[A], bool]) -> bool:
    """Renvoie `True` si au moins un élément de `liste` vérifie le prédicat `p`
    et `False` sinon.
    Précondition : chacun des éléments de `liste` vérifie la
                   précondition de `p`
    $$$ def est_superieur_a_2(n: int) -> bool: return n > 2
    $$$ il_existe(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_superieur_a_2)
    True
    $$$ def est_negatif(n: int) -> bool: return n <= 0
    $$$ il_existe(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_negatif)
    False
    $$$ def aime_les_tris(x): return True # tout le monde aime les tris. Sisi !
    $$$ il_existe(ApLst(), aime_les_tris)
    False
    """
    ...

def filtre(liste: ApLst, p: Callable[[A], bool]) -> ApLst:
    """Renvoie la liste des éléments de `liste` vérifiant le prédicat `p`
    Précondition : chacun des éléments de `liste` vérifie la
                   précondition de `p`
    $$$ def est_superieur_a_2(n: int) -> bool: return n > 2
    $$$ filtre(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_superieur_a_2)
    ApLst(3, ApLst(4, ApLst()))
    $$$ def est_pair(n: int) -> bool: return n % 2 == 0
    $$$ filtre(ApLst(3, ApLst(1, ApLst(4, ApLst()))), est_superieur_a_2)
    """
    ...

def reduction(liste: ApLst, f: Callable[[A, A], A]) -> A:
    """Renvoie la *réduction* de `liste` par `f`.
    Par exemple, si `liste` contient `x1`, `x2`, `x3`, `x4` et `x5`,
    le réduction de `liste` par `f` est : `f(x1, f(x2, f(x3, f(x4, x5)))))`
    Précondition : la précondition de `f` est vérifiée à chaque étape
                   de la réduction
    Exemples:
    $$$ reduction(ApLst(3, ApLst(1, ApLst(4, ApLst()))), min)
    1
    $$$ def add(x, y): return x + y
    $$$ reduction(ApLst(3, ApLst(1, ApLst(4, ApLst()))), add)
    8
    $$$ def base10(unite, dizaines): return unite + 10*dizaines
    $$$ reduction(ApLst(3, ApLst(1, ApLst(4, ApLst()))), base10)
    413
    """
    ...

def applications_successives(x: A, f: Callable[[A], A], n: int) -> ApLst:
    """Renvoie la liste des applications successives de `f` sur `x`
    jusqu'à ce que `f` soit appliquée n fois.
    Précondition : `n >= 0` et `x`, `f(x)``, ..., `f(f(...(f(x))))`` vérifient
                   la précondition de `f`
    Exemples
    $$$ def double(n): return 2*n
    $$$ applications_successives(1, double, 5)
    ApLst(1, ApLst(2, ApLst(4, ApLst(8, ApLst(16, ApLst(32, ApLst()))))))
    """
    ...

