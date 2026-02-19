from ap_decorators import *
import matplotlib.pyplot as plt
import numpy as np
from compare import compare
from algo_recherches import *
from random import choice, randint
from genere_listes import genere_lint_croissante
comp_count = count(compare)
def calcul_cout_moyen_rech_fructueuse(liste:list[int],entier:int,
                                      recherche:callable([int,list[int],int,int,[[int, int], int], bool ]))->float:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    moyen=0.
    comp_count.counter = 0
    for _  in range(entier):
        elt= choice(liste)
        recherche(elt,liste,0,None,comp_count)
    return comp_count.counter/entier
            
def calcul_cout_moyen_rech_infructueuse(liste:list[int],entier:int,
                                      recherche:callable([int,list[int],int,int,[[int, int], int], bool ]))->float:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    moyen=0.
    comp_count.counter = 0
    for _  in range(entier):
        elt= randint(0,100)*2+1
        recherche(elt,liste,0,None,comp_count)
    return comp_count.counter/entier





if __name__ == '__main__':
   liste_recher=[recherche_seq,recherche_seq_rec,recherche_seq_triee,recherche_seq_triee_rec,
                   recherche_dicho,recherche_dicho_rec]
   liste_comp=[calcul_cout_moyen_rech_fructueuse,calcul_cout_moyen_rech_infructueuse]
   resultat=[]
   for i in range(6):
       resultat_fructueuse=[]
       resultat_infructueuse=[]
       for j in range(1,101):
           liste_int=genere_lint_croissante(j)
           resultat_fructueuse.append(liste_comp[0](liste_int,j,liste_recher[i]))
           resultat_infructueuse.append(liste_comp[1](liste_int,j,liste_recher[i]))
       resultat.append(resultat_fructueuse)
       resultat.append(resultat_infructueuse)
       
    
    
   abscisses = [i for i in range(1,101)]
   colors=plt.cm.tab20(np.linspace(0,1,12))
   for i in range(len(resultat)):
       plt.plot(abscisses, resultat[i], color=colors[i], label=f" courbe {i+1}")
       plt.legend(ncol=3)
   plt.show()

       
           
           
           
       
       
       
       
   