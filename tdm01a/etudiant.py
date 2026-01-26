#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:author: FIL - FST - Univ. Lille.fr <http://portail.fil.univ-lille.fr>_
:date: janvier 2019
:last revised: janvier 2026
:Fournit :
"""
from ue import Ue


class Etudiant:
    """
    une classe représentant des étudiants.

    $$$ etu = Etudiant(314159, 'Oléon', 'Tim', 'tim.oleon@univ-lille.fr')
    $$$ str(etu)
    'Tim Oléon'
    $$$ repr(etu)
    "Etudiant(314159, 'Oléon', 'Tim', 'tim.oleon@univ-lille.fr')"
    $$$ etu.prenom
    'Tim'
    $$$ etu.nip
    314159
    $$$ etu.nom
    'Oléon'
    $$$ etu.email
    'tim.oleon@univ-lille.fr'
    $$$ etu.ues
    []
    $$$ etu2 = Etudiant(314159, 'Oléon', 'Tim', 'tim.oleon@univ-lille.fr')
    $$$ etu == etu2
    True
    $$$ etu3 = Etudiant(141442, 'Oléon', 'Tim', 'tim.oleon@univ-lille.fr')
    $$$ etu == etu3
    False
    """
    def __init__(self, nip: int, nom: str, prenom: str, email: str):
        """
        initialise un nouvel étudiant à partir de son nip, son nom, son
        prénom et son email

        précondition : le nip, le nom et le prénom ne peuvent être nuls ou vides.
        """
        self.nip=nip
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.ues=[]
        assert self.nip and self.nom and self.prenom and self.email,"Invalid input"

    def __eq__(self, other) -> bool:
        """
        Renvoie True ssi other est un étudiant ayant :
        - même nip,
        - même nom et
        - même prénom que `self`,
        et False sinon.
        """
        if isinstance(other, Etudiant) and isinstance(self, Etudiant):
            if self.nom == other.nom and self.prenom == other.prenom and self.nip==other.nip:
                return True
        return False

    def __str__(self) -> str:
        """
        Renvoie une représentation textuelle de self pour impression.
        """
        return f"{self.prenom} {self.nom}"

    def __repr__(self) -> str:
        """
        Renvoie une représentation textuelle interne de self pour le shell.
        """
        return f"Etudiant({self.nip}, '{self.nom}', '{self.prenom}', '{self.email}')"

    def add_ue(self, ue: Ue):
        """Ajoute une ue à la liste des ues suivies par cet étudiant.
        """
        assert  ue not in self.ues, "ue existe deja dans la liste des ues suivies"
        self.ues.append(ue)

if __name__ == "__main__":
    import l1test
    l1test.testmod('etudiant.py')


