from scientifique import *
from tdm07_symbolique import *
from tdm07_symbolique.annexe_tris import *
from tdm07_symbolique.tris import *


def decoupe_ligne_scientifique(ligne:str):
    """ 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    ligne=ligne.strip()
    l=ligne.split(";")
    anne=l[2].split("-")
    return Scientifique(l[0],l[1],anne[0],anne[1],l[3])

def lire_csv_scientifiques(fichier:str):
    """ 
    Précondition : 
    Exemple(s) :
    $$$ 
    """
    with open(fichier,"r") as f:
        entete=f.readline()
        liste_scientifique=f.readlines()
    return liste_scientifique




if __name__ == '__main__':
    liste_scientifique=lire_csv_scientifiques("femmes-scientifiques.csv")
    
    for i in range(5):
        print(decoupe_ligne_scientifique(liste_scientifique[i]))
    
    tri_select(liste_scientifique,Scientifique.comparaison_nom)
        
        
    