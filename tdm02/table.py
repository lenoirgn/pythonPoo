#!/usr/bin/env python3

from association import Association

# un objet blanc pour indiquer une suppression dans la table
FANTOME = object()


def est_cellule_vide(table: list[any], indice: int, fantome_est_vide: bool = False) -> bool:
    """Renvoie True ssi la cellule d'indice `indice` est vide.

    Une cellule vide contenant None est toujours considérée comme vide.
    Une cellule contenant FANTOME est considérée comme vide si et seulement si fantome_est_vide vaut True

    précondition: 0 <= i < len(table)

    Exemples:

    $$$ t = [0, None, 1, FANTOME, 2, None]
    $$$ [est_cellule_vide(t, i) for i in range(len(t))]
    [False, True, False, False, False, True]
    $$$ [est_cellule_vide(t, i, True) for i in range(len(t))]
    [False, True, False, True, False, True]    
    """
    return ( table[indice] != None ) or ( table[indice] ==FANTOME and fantome_est_vide)






def nombre_de_cellules_non_vides(table: list[any]) -> int:
    """Renvoie le nombre de cellules non vides de la table.

    Dans cette fonction, une cellule vide est associée à soit None, soit FANTOME.

    Précondition : \

    Exemples:

    $$$ nombre_de_non_vides([1, None, 2, FANTOME, 3])
    3
    """
    comp=0
    for i in range (len(table)):
        if est_cellule_vide(table, i,fantome_est_vide=False):
            comp += 1
    return comp


def table_indice(table: list[any], cle: C,
                 fantome_est_vide: bool = False,
                 primaire: Callable[[any], int] = hash) -> int:
    """Renvoie l'indice possible de cle.

    `primaire` est une fonction associant un entier à une clé, par défaut
    on utilise hash.

    On initialise l'indice à primaire(cle) % len(table), puis on recherche dans la
    table à partir de cet entier une cellule vide OU une cellule contenant
    une association dont la cle vaut `cle`.

    $$$ table = [None] * 10
    $$$ ind1 = hash("chat") % 10
    $$$ table_indice(table, "chat")
    ind1
    $$$ table[ind1] = Association("chat", "croquettes")
    $$$ ind2 = table_indice(table, "chien", False, lambda x: ind1)
    $$$ ind2
    (ind1 + 1) % 10
    $$$ table[ind2] = Association("chien", "viande")
    $$$ table_indice(table, "chien", False, lambda x: ind1)
    ind2
    $$$ ind3 = table_indice(table, "poney", False, lambda x: ind1)
    $$$ ind3
    (ind1 + 2) % 10
    $$$ table[ind2] = FANTOME
    $$$ table_indice(table, "poney", False, lambda x: ind1)
    ind3
    $$$ table_indice(table, "chien", True, lambda x: ind1)
    ind2
    $$$ table_indice(table, "chien", False, lambda x: ind1)
    ind3
    """
    indice=table[primaire]%len(table)
    for i in range (indice,len(table)):
        if est_cellule_vide(table,i,fantome_est_vide) or table[i].cle ==cle:
            return i




if __name__ == '__main__':
    import l1test
    l1test.testmod('table.py')

