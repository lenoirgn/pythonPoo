#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - Faculté des Sciences et Technologies
:date: février 2026
:dernière révision:
"""

class Scientifique:
    """ Classe pour mémoriser des informations sur des sicentifiques, avec les attribus suivants :
    nom, prénom, date de naissance, date de mort, activité

    Exemple(s) :
    $$$ ada = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
    $$$ ada
    Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
    """

    def __init__(self, prenom: str, nom: str, naissance: int, mort: int, activite:str):
        """ Initialise un objet de type Scientifique
        Exemple(s) :
        $$$ ada = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        $$$ ada.nom
        "Lovelace"
        $$$ ada.naissance
        1815
        $$$ ada.prenom
        "Ada"
        $$$ ada.activite
        "Informaticienne"
        $$$ ada.mort
        1852
        """
        self.prenom=prenom
        self.nom=nom
        self.naissance=naissance
        self.mort=mort
        self.activite=activite

    def __repr__(self)->str:
        """ Renvoie la chaine qui représente un ou une scientifique

        Exemple(s) :
        $$$ ada = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        $$$ repr(ada)
        'Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")'
        """
        return f'Scientifique("{self.prenom}", "{self.nom}", {self.naissance}, {self.mort},"{self.activite}")'

    def __str__(self)->str:
        """ Renvoie la chaine qui permet d'afficher un ou une scientifique

        Exemple(s) :
        $$$ ada = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        $$$ str(ada)
        'Ada Lovelace (1815-1852) Informaticienne'
        """
        return f"{self.prenom} {self.nom} ({self.naissance}-{self.mort}) {self.activite}"


    def __eq__(self, other:"Scientifique")->bool:
        """ Renvoie True si tous les attributs des 2 scientifiques sont identiques,
        renvoie False si au moins un est différent ou si l'objet de gauche n'est pas un ou une Scientifique

        Exemple(s) :
        $$$ ada = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        $$$ ada == ("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        False
        $$$ ada2 = Scientifique("Ada", "Lovelace", 1815, 1852, "Informaticienne")
        $$$ ada == ada2
        True
        $$$ ada2.nom = "Byron"
        $$$ ada == ada2
        False
        """
        if isinstance(other,Scientifique):
            if self.nom==other.nom:
                if self.prenom==other.prenom:
                    if self.naissance==other.naissance:
                        if self.mort==other.mort:
                            if self.activite==other.activite:
                                return True
        return False
    def comparaison_nom(self, other:"Scientifique")->int:
        """ 
        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Scientifique):
            if self.nom>other.nom:
                return 1
            elif self.nom<other.nom:
                return -1
            else:
                return 1
    def comparaison_naissance(self, other:"Scientifique")->int:
        """ 
        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Scientifique):
            if self.naissance>other.naissance:
                return 1
            elif self.naissance<other.naissance:
                return -1
            else:
                return 1
    def comparaison_activite(self, other:"Scientifique")->int:
        """ 
        Précondition : 
        Exemple(s) :
        $$$ 
        """
        if isinstance(other,Scientifique):
            if self.activite>other.activite:
                return 1
            elif self.activite<other.activite:
                return -1
            else:
                return 1
        


            
        

