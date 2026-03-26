VIDE="vide"
class Arbre:
    def __init__(self,e:"Any"=None,g:"Arbre"=None,d:"Arbre"=None):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ A=Arbre(0,VIDE,VIDE)
        $$$ A.e
        0
        
    
        """
        if e is None:
            self.content=(VIDE)
        else:
            self.content=e
            if g is None :
                g.content=(VIDE)
            elif d is None :
                d.content=(VIDE)
            else:
                self.g=g
                self.d=d
    def est_vide(self):
        """
        Précondition : 
        Exemple(s) :
        $$$ A=Arbre(0,VIDE,VIDE)
        $$$ A.est_vide()
        False
        $$$ B=Arbre()
        $$$ B.est_vide()
        True
        
        """
        return self.content==VIDE
    
    def __eq__(self,other):
        """ à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ A=Arbre(0,VIDE,VIDE)
        $$$ B=Arbre(0,VIDE,VIDE)
        $$$ C=Arbre(0,A,B)
        $$$ A==B
        True
        $$$ C==A
        False
        """
        if isinstance(other,Arbre):
            if self.est_vide() and other.est_vide():
                return True
            elif self.est_vide() or other.est_vide():
                return False
            elif self.content != other.content:
                return False
            else:
                return  self.d==other.d and  self.g==other.g
        else:
           return False
    
        
          
        
    