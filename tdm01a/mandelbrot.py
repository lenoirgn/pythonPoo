#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2026
:Fournit :
"""
from math import sqrt
from complexes import Complexe

def est_bornee(c: Complexe) -> bool:
    """Renvoie vrai si et seulement si les cinquante premiers termes
    de la suite (z_n)_n défine par :
       - z_0 = 0
       - z_{n+1} = z_n² + c
    sont tous de modules inférieur à 2
    Précondition : aucune
    $$$ est_bornee(Complexe(0.0, 0.0))
    True
    $$$ est_bornee(Complexe(1.0, 0.0))
    False 
    """
    z_complexe=Complexe(0.,0.)
    for i in range(50):
        z_complexe*=z_complexe
        z_complexe = z_complexe + c
        if not sqrt(Complexe.carre_module(z_complexe))<2:
            return False
    return True
       
est_bornee( Complexe(-1.0, -1.0))     

class Mandelbrot:
    """Attributs et méthodes permettant de définir une tabulation
    finie de l'ensemble de Mandelbrot.
    """
    def __init__(self, bas_gauche: Complexe, haut_droite: Complexe,
                       nb_subd_reelle: int, nb_subd_imaginaire: int):
        """Crée une instance contenant la tabulation du sous-ensemble
        de Mandelbrot pour les c_n,p = bas_gauche + n x + p i y avec :
           - 0 <= n < nb_subd_reelle
           - 0 <= p < nb_subd_imaginaire
           - x = partie réelle de (haut_droite - bas_gauche) / (nb_subd_reelle - 1)
           - y = partie imaginaire de (haut_droite - bas_gauche) / (nb_subd_imaginaire - 1)
        Cette instance aura de plus deux attribut calculés : `pas_reel` de valeur x
        et `pas_imaginaire` de valeur y.
        Précondition :
         - nb_subd_reelle > 1
         - nb_subd_imaginaire > 1
         - partie réelle de haut_droite > partie réelle de bas_gauche
         - partie imaginaire de haut_droite > partie imaginaire de bas_gauche
        $$$ ensemble1 = Mandelbrot(Complexe(-2., -1.), Complexe(1., 1.), 4, 3)
        $$$ ensemble1.bas_gauche
        Complexe(-2.0, -1.0)
        $$$ ensemble1.haut_droite
        Complexe(1.0, 1.0)
        $$$ ensemble1.nb_subd_reelle
        4
        $$$ ensemble1.nb_subd_imaginaire
        3
        $$$ ensemble1.pas_reel
        1.0
        $$$ ensemble1.pas_imaginaire
        1.0
        """
        
        self.bas_gauche = bas_gauche
        self.haut_droite = haut_droite
        self.nb_subd_reelle = nb_subd_reelle
        self.nb_subd_imaginaire = nb_subd_imaginaire
        self.pas_reel=(self.haut_droite.reelle-self.bas_gauche.reelle)/(nb_subd_reelle-1)
        self.pas_imaginaire=(self.haut_droite.imaginaire-self.bas_gauche.imaginaire)/(nb_subd_imaginaire-1)

    def liste_appartenance(self) -> list[list[bool]]:
        """Renvoie une grille de booléens permettant de connaitre l'appartenance
        à l'ensemble de Mandelbrot des nombres tabulés dans `self`.
        Postcondition : pour tout couple d'indices valides (n, p)
         self.liste_appartenance()[p][n] est vrai ssi est_bornee(c) est vrai
         avec c = self.bas_gauche + n * self.pas_reel + i * p * self.pas_imaginaire
        Précondition : aucune
        $$$ ensemble1 = Mandelbrot(Complexe(-2., -1.), Complexe(1., 1.), 4, 3)
        $$$ ensemble1.liste_appartenance()
        [[False, False, True, False], \
         [False, True, True, False], \
         [False, False, True, False]]
        """
        grille=[]
        for p in range(self.nb_subd_imaginaire):
            ligne=[]
            for n in range(self.nb_subd_reelle):
                c=Complexe(self.bas_gauche.reelle+(n*self.pas_reel),self.bas_gauche.imaginaire+(p*self.pas_imaginaire))
                res=est_bornee(c)
                ligne.append(res)
            grille.append(ligne)
        return grille


    def translation(self, nb_pas_reelle: int, nb_pas_imaginaire: int):
        """Cree une instance de Mandelbrot qui possède les mêmes nombres
        de subdivision que `self`, mais dont les attributs bas_gauche
        et haut_droite sont translatés de z avec
        z = nb_pas_reelle * self.pas_reelle + i * nb_pas_imaginaire * self.pas_imaginaire
        Précondition : aucune
        $$$ ensemble1 = Mandelbrot(Complexe(-2., -1.), Complexe(1., 1.), 7, 5)
        $$$ trans = ensemble1.translation(1, -2)
        $$$ trans.bas_gauche
        Complexe(-1.5, -2.0)
        $$$ trans.haut_droite
        Complexe(1.5, 0.0)
        """

        z=Complexe(nb_pas_reelle * self.pas_reel,nb_pas_imaginaire * self.pas_imaginaire)
        return Mandelbrot(self.bas_gauche+z,self.haut_droite+z,self.nb_subd_reelle,self.nb_subd_imaginaire)

    def zoom(self, coefficient: int, nb_pas_reelle: int, nb_pas_imaginaire: int):
        """Crée une instance de Mandelbrot qui possède les mêmes nombres de
        subdivisions que `self`, mais centrée sur
        z = self.bas_gauche + nb_pas_reelle * self.pas_reelle
                            + i * nb_pas_imaginaire * self.pas_imaginaire
        et avec les attribut pas_reelle et pas_imaginaires égaux à ceux de
        self divisés par coefficient.
        Précondition : coeffcient > 0
        $$$ ensemble1 = Mandelbrot(Complexe(-2., -1.), Complexe(1., 1.), 7, 5)
        $$$ agrand = ensemble1.zoom(2, 4, 2) # on zoome autour de 0 + i*0
        $$$ agrand.bas_gauche
        Complexe(-0.75, -0.5)
        $$$ agrand.haut_droite
        Complexe(0.75, 0.5)
        """
        z = Complexe(self.bas_gauche.reelle + nb_pas_reelle * self.pas_reel,self.bas_gauche.imaginaire + nb_pas_imaginaire * self.pas_imaginaire)
        pas_reelle_new = self.pas_reel / coefficient
        pas_imaginaire_new = self.pas_imaginaire / coefficient
        bas_gauche_new = Complexe(z.reelle - (self.nb_subd_reelle - 1)/2 * pas_reelle_new,z.imaginaire - (self.nb_subd_imaginaire - 1)/2 * pas_imaginaire_new)
        haut_droite_new = Complexe(z.reelle+ (self.nb_subd_reelle - 1)/2 * pas_reelle_new,z.imaginaire+ (self.nb_subd_imaginaire - 1)/2 * pas_imaginaire_new)
        return Mandelbrot(bas_gauche_new,haut_droite_new,self.nb_subd_reelle,self.nb_subd_imaginaire)



          

