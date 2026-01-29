#!/usr/bin/env python3
from operator import index

from etudiant import Etudiant
from date import Date
from heure import Heure
from salle import Salle
from ue import Ue
from creneau import Creneau


def recherche_etudiant(nip: int, etudiants: list[Etudiant]) -> Etudiant | None:
    """Renvoie l'étudiant de la liste dont le nip est `nip` si un tel étudiant existe
    et None sinon.

    précondition : \

    exemples :

    """
    for etudiant in etudiants:
        if etudiant.nip==nip:
            return etudiant
    return None

def emploi_du_temps(nip: int, etudiants: list[Etudiant], creneaux: list[Creneau]) -> list[Creneau]:
    """Renvoie la liste des créneaux pour un étudiant."""
    etudiant = recherche_etudiant(nip,etudiants)
    liste_creneaux = []
    for creneau in creneaux:
        if creneau.ue==etudiant.ue:
            liste_creneaux.append(creneau)
    return liste_creneaux





def presents(cren: Creneau, etudiants: list[Etudiant]) -> list[Etudiant]:
    """Renvoie la liste des étudiants devant assister au créneau.
    """
    liste_presents = []
    for etudiant in etudiants:
        liste_creneaux_etudiant=emploi_du_temps(etudiant.nip,etudiants,liste_creneaux)
        if cren in liste_creneaux_etudiant:
            liste_presents.append(etudiant)
    return liste_presents




