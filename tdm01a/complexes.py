#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2026
:Fournit : une classe permettant de travailler simplement avec les complexes
"""
from math import sqrt
class Complexe:
    """Classe permettant de travailler simplement avec des nombres complexes
    """
    def __init__(self, partie_reelle: float, partie_imaginaire: float):
        """Crée une instance d'un nombre complexe :
              - de partie réelle `partie_reelle`
              - de partie imaginaire `partie_imaginaire`.
        Les attributs respectifs sont `reelle` et `imaginaire`.
        Précondition : aucune
        $$$ z = Complexe(2., -.5)
        $$$ z.reelle
        2.0
        $$$ z.imaginaire
        -0.5
        """
        self.reelle=partie_reelle
        self.imaginaire=partie_imaginaire

    def __repr__(self) -> str:
        """Renvoie une représentation de `self`.
        Précondition : aucune
        $$$ z = Complexe(2., -.5)
        $$$ repr(z)
        'Complexe(2.0, -0.5)'
        """
        return f"Complexe({self.reelle}, {self.imaginaire})"

    def __eq__(self, other) -> bool:
        """Renvoie vrai si et seulement si other est une instance d'un nombre
        complexe et self et other ont même partie réelle et même partie
        imaginaire.
        Précondition : aucune
        $$$ Complexe(1.0, 0.0) == 1.0
        False
        $$$ Complexe(2.0, -0.5) == Complexe(2.0, -0.5)
        True
        $$$ Complexe(2.0, -0.5) == Complexe(-1.0, -0.5)
        False
        $$$ Complexe(2.0, -0.5) == Complexe(2.0, 1.0)
        False
        $$$ Complexe(2.0, -0.5) == Complexe(-1.0, 1.0)
        False
        """
        return (isinstance(self,Complexe) and isinstance(other, Complexe)) and self.reelle==other.reelle and self.imaginaire==other.imaginaire
            

    def __add__(self, z):
        """Renvoie self + other
        Précondition : aucune
        $$$ Complexe(2.0, -0.5) + Complexe(-1.0, 1.0)
        Complexe(1.0, 0.5)
        """
        return Complexe(self.reelle+z.reelle,self.imaginaire+z.imaginaire)
    def __sub__(self, z):
        """Renvoie self - other
        Précondition : aucune
        $$$ Complexe(2.0, -0.5) - Complexe(-1.0, 1.0)
        Complexe(3.0, -1.5)
        """
        return Complexe(self.reelle-z.reelle,self.imaginaire-z.imaginaire)

    def __rmul__(self, x: float):
        """Renvoie x*self avec x réel (flottant)
        Précondition : aucune
        $$$ 3.0 * Complexe(2.0, -0.5)
        Complexe(6.0, -1.5)
        """
        return Complexe(x*self.reelle,x*self.imaginaire)

    def __mul__(self, z):
        """Renvoie self * other
        Précondition : aucune
        $$$ Complexe(2.0, -0.5) * Complexe(-1.0, 1.0)
        Complexe(-1.5, 2.5)
        """
        return Complexe(self.reelle*z.reelle -self.imaginaire*z.imaginaire,self.reelle*z.imaginaire +self.imaginaire*z.reelle)

    def carre_module(self) -> float:
        """Renvoie le carré du module de self
        Précondition: aucune
        $$$ Complexe(2.0, -0.5).carre_module()
        4.25
        """
        return self.reelle**2+self.imaginaire**2


