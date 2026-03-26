class CarteTopographique:
    def __init__(self,nom:str,valeur_al:list[list[float]]):
        """ 
        Précondition : 
        Exemple(s) :
        $$$ region= CarteTopographique("ici",[[3.,-7,6],[3.,-7,6],[3.,-7,6]])
        $$$ region.nom
        "ici"
        $$$ region.valeur_al
        [[3.,-7,6],[3.,-7,6],[3.,-7,6]]
        """
        self.nom=nom
        self.valeur_al=valeur_al
    def __str__(self):
        """
        Précondition : 
        Exemple(s) :
        $$$ region= CarteTopographique("ici",[[3.,-7,6],[3.,-7,6],[3.,-7,6]])
        $$$ str(region)
        'CarteTopographique de : ici, 3x3 cases'
        """
        return f"CarteTopographique de : {self.nom}, {len(self.valeur_al)}x{len(self.valeur_al[0])} cases"
    def altitude_case(self, x:float,y:float):
        """ 

        Précondition : 
        Exemple(s) :
        $$$ region= CarteTopographique("ici",[[3.,-7,6],[3.,-7,6],[3.,-7,6]])
        $$$ region.altitude_case(0,0)
        3.0  
        
        """
        if x<len(self.valeur_al) and y<len(self.valeur_al[0]):
            return self.valeur_al[x][y]
        else:
            raise ValueError("Ivalid")
    def affiche_carte(self):
        """ 

        Précondition : 
        Exemple(s) :
       
        """
        if len(self.valeur_al)<10 or len(self.valeur_al[0])<10:
            for i in range(len(self.valeur_al)):
                ligne=""
                for j in range(len(self.valeur_al[0])):
                    ligne+=str(self.valeur_al[i][j]) + "\t"
                print(ligne)
    def __add__(self,other):
        """

        Précondition : len(self.valeur_al)==len(other.valeur_al) and len(self.valeur_al[0])==len(other.valeur_al[0])
        Exemple(s) :
        $$$ region= CarteTopographique("ici",[[3.,-7,6],[3.,-7,6],[3.,-7,6]])
        $$$ variante= CarteTopographique("ici",[[0,1,0],[0,1,0],[0,1,0]])
        $$$ update=region+variante
        $$$ ok=CarteTopographique("ici",[[3.,-6,6],[3.,-6,6],[3.,-6,6]])
        $$$ ok.affiche_carte()==update.affiche_carte()
        True
        
        """
        if isinstance(other,CarteTopographique):
            lres=[]
            for i in range(len(self.valeur_al)):
                ligne=[]
                for j in range(len(self.valeur_al[0])):
                    col=self.valeur_al[i][j]+other.valeur_al[i][j]
                    ligne.append(col)
                    col=0
                lres.append(ligne)
        return CarteTopographique(self.nom,lres)
class Inondation:
    def __init__(self,nb_ligne=int,nb_col=int,liste=list[tuple[int,int]]):
        """ 

        Précondition : 
        Exemple(s) :
        $$$ I=Inondation(3,4,[(1,0),(1,1),(2,0)])
        $$$ I.nb_ligne
        3
        $$$ I.nb_col
        4
        $$$ I.liste
        [(1,0),(1,1),(2,0)]
        """
        self.nb_ligne=nb_ligne
        self.nb_col=nb_col
        self.liste=liste
    def __str__(self):
        """
        Précondition : 
        Exemple(s) :
        $$$ I=Inondation(3,4,[(1,0),(1,1),(2,0)])
        $$$ str(I)
        "Inondation de taille 3x4, avec 3 points inondes"
        """
        return f"Inondation de taille {self.nb_ligne}x{self.nb_col}, avec {len(self.liste)} points inondes"
        
        
    def est_inonde(self,point:tuple[int,int]):
            """ à_remplacer_par_ce_que_fait_la_fonction

            Précondition : 
            Exemple(s) :
            $$$ 
            $$$ I.est_inonde((0,0))
            False
            $$$ I.est_inonde((1,0))
            True
            """
            return point in self.liste
    def affiche_inondation(self):
        """ 

        Précondition : 
        Exemple(s) :
        $$$ 
        """
        for i in range(self.nb_ligne):
            ligne=""
            for j in range(self.nb_col):
                if self.est_inonde((i,j)):
                    ligne+="X"
                else:
                    ligne+="."
            print(ligne+"\n")
        
    def etend(self, liste=list[tuple[int,int]]):
        """ 
        Précondition : 
        Exemple(s) :
        $$$ I=Inondation(3,4,[(1,0),(1,1),(2,0)])
        $$$ I.etend([(1,0),(1,1),(2,0),(0,0)])
        $$$ j=Inondation(3,4,[(1,0),(1,1),(2,0),(0,0)])
        $$$ I.affiche_inondation==j.affiche_inondation
        True
    
        """
        for el in liste:
            if not el in self.liste:
                self.liste.append(el)
                
            
            
        
    
    
        
        
        
    
        
                
        
        
#         
    