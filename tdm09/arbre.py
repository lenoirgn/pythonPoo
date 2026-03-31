       
from typing import TypeVar
from collections.abc import Callable
from aplst import ApLst
class ArbrError(Exception):
    """ à_remplacer_par_ce_que_fait_la_classe

    Exemple(s) :
    $$$ 
    """
    def init(self, msg:str):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        self.msg = msg
        
class Arbre():
    """ à_remplacer_par_ce_que_fait_la_classe

    Exemple(s) :
    $$$ v = Arbre()
    $$$ a = Arbre(1, Arbre(2, v, v), v)
    $$$ b = Arbre(1, v, Arbre(2, v, v))
    $$$ a.gauche()
    Arbre(2, Arbre(), Arbre())
    $$$ a.droit()
    Arbre()
    $$$ b.gauche().is_empty()
    True
    $$$ a.gauche().is_empty()
    False
    $$$ a.etiquette()
    1
    
    """
    def __init__(self, etiquette: int=None, gauche:"Arbre"= None, droite:"Arbre"= None):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ v = Arbre()
        $$$ a = Arbre(1, Arbre(2, v, v), v)
        $$$ b = Arbre(1, v, Arbre(2, v, v))
        
        """
        if etiquette is None and gauche is None and droite is None:
            self.content = ()
        elif etiquette is None and (gauche is not None or droite is not None):
            raise ArbrError("Arbre inexistant")
        elif (gauche is not None and not isinstance(gauche, Arbre)) or \
         (droite is not None and not isinstance(droite, Arbre)):
            raise ArbrError("mauvais arguments")
        else:
        # si gauche ou droite est None → on met un arbre vide
            if gauche is None:
                gauche = Arbre()
            if droite is None:
                droite = Arbre()

            self.content = (etiquette, gauche, droite)
            
    def is_empty(self)->bool:
        """ renvoie True si self est vide et False sinon

        Précondition : 
        Exemple(s) :
        $$$ v = Arbre()
        $$$ a = Arbre(1, Arbre(2, v, v), v)
        $$$ b = Arbre(1, v, Arbre(2, v, v))
        $$$ a.is_empty()
        False
        $$$ b.gauche().is_empty()
        True
        """
        return len(self.content) == 0
            
    def gauche(self):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ a = Arbre(1, Arbre(2, Arbre(), Arbre()), Arbre())
        $$$ a.gauche()
        Arbre(2, Arbre(), Arbre())
        """
        if self.is_empty():
            raise ArbrError("arbre inexistant")
        return self.content[1]
    
    def droit(self):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if self.is_empty():
            raise ArbrError("arbre inexistant")
        return self.content[2]
    
    def etiquette(self):
        """ renvoie l'etiquette

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if self.is_empty():
            raise ArbrError("arbre inexistant")
        return self.content[0]
        
    def __str__(self) ->str:
        """renvoie une representation textuelle de self

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if self.is_empty():
            return Arbre()
        return f'Arbre({self.etiquette}, {self.gauche}, {self.droite})'
    
    def __eq__(self, other)->bool:
        """ renvoie True si self = other

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if not isinstance(other, Arbre):
            return False
        if self.is_empty() and other.is_empty():
            return True
        return self.etiquette() == other.etiquette() and self.gauche() == other.gauche() and self.droit() == other.droit()
        
def nombre_noeuds(a) ->int:
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ v = Arbre()
        $$$ a = Arbre(1, Arbre(2, v, v), v)
        $$$ nombre_noeuds(a)
        2
        """
        if a.is_empty():
            return 0
        return 1+nombre_noeuds(a.gauche()) + nombre_noeuds(a.droit())

def hauteur(a: Arbre) ->int:
    """ renvoie la hauteur de l'arbre

    Précondition : 
    Exemple(s) :
    $$$ v = Arbre()
    $$$ a = Arbre(1, Arbre(2, v, v), v)
    $$$ hauteur(a)
    2
    """
    if a.is_empty():
        return 0
    g = hauteur(a.gauche())
    d = hauteur(a.droit())
    return 1+max(g, d)
def est_feuille(a:Arbre) ->bool:
    """renvoie True si a est une feuille False sinon

    Précondition : 
    Exemple(s) :
    $$$ v = Arbre()
    $$$ a = Arbre(1, Arbre(2, v, v), v)
    $$$ est_feuille(a)
    False
    $$$ est_feuille(Arbre(1,v, v))
    True
    """
    if a.is_empty():
        raise ArbrError("arbre inexistant")
    return a.gauche().is_empty() and a.droit().is_empty()

def concat(l1: ApLst, l2: ApLst) ->ApLst:
    """renvoie la concatenation de l1 et l2

    Précondition : 
    Exemple(s) : 
    $$$ concat((ApLst(3, ApLst(1, ApLst(4, ApLst())))), ApLst(3, ApLst(1, ApLst())))
    ApLst(3, ApLst(1, ApLst(4, ApLst(3, ApLst(1, ApLst())))))
    """
    if l1.is_empty():
        return l2
    return ApLst(l1.head(), concat(l1.tail(), l2))
def etiquettes(arbre: Arbre) ->ApLst:
    """renvoie la liste récursive de étiquettes de arbre et de ses descendants

    Précondition : 
    Exemple(s) :
    $$$ v = Arbre()
    $$$ a = Arbre(1, Arbre(2, v, v), v)
    $$$ etiquettes(a)
    ApLst(2, ApLst(1,ApLst()))
    """
    if arbre.is_empty():
        return ApLst()
    else:
        return concat(etiquettes(arbre.gauche()), ApLst(arbre.etiquette(), etiquettes(arbre.droit())))
