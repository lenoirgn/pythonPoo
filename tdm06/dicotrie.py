
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
:mod:`dicotrie` module : un module pour les ensembles d'associations
:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_
:date: 2026 février
"""
from association import Association, C, V, comp_asso
from recherche_dicho import indice_dicho, inserer,compare
from types import NoneType
class DicoTrie:
    """Classe d'une association clé-valeur
    """
    def __init__(self, liste_assos: list[Association]):
        """
        """
        self.liste_assos=[]
        for assos in liste_assos:
            self[assos.cle]=assos.valeur
    def __repr__(self) -> str:
        """
        $$$ repr(DicoTrie([Association('a', 1)]))
        "DicoTrie([Association('a', 1)])"
        $$$ repr(DicoTrie([Association('a', 1), Association('b', 2)]))
        "DicoTrie([Association('a', 1), Association('b', 2)])"
        $$$ repr(DicoTrie([Association('c', 3), Association('a', 2), Association('b', 1)]))
        "DicoTrie([Association('a', 2), Association('b', 1), Association('c', 3)])"
        """
        return f"DicoTrie({self.liste_assos})"
    def __eq__(self, autre) -> bool:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d2 = DicoTrie([Association("b", 2), Association("a", 1)])
        $$$ d3 = DicoTrie([Association("a", 1), Association("b", 2), Association("c", 3)])
        $$$ d1 == d2
        True
        $$$ d1 == d3
        False
        $$$ d1 == {"a": 1, "b": 2}
        False
        """
        if not isinstance(autre, DicoTrie):
            return False
        if len(self.liste_assos)!=len(autre.liste_assos):
            return False
        for assos in self.liste_assos:
            if assos not in autre.liste_assos:
                return False
        return True
    def __setitem__(self, cle: C, valeur: V) -> NoneType:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d1["c"] = 3
        $$$ d1
        DicoTrie([Association("a", 1), Association("b", 2), Association("c", 3)])
        """
        l_cles = []
        for assos in self.liste_assos:
            l_cles.append(assos.cle)
            if assos.cle == cle:
                assos.valeur = valeur
        trouve, ind = indice_dicho(cle, l_cles, compare)
        inserer(ind, Association(cle, valeur), self.liste_assos)
    def __getitem__(self, cle: C) -> V:
        """
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)])
        $$$ d1['a']
        1
        $$$ d1['b']
        2
        $$e d1['c']
        KeyError
        """
        trouve=False
        for assos in self.liste_assos:
            if assos.cle==cle:
                trouve=True
                return assos.valeur
        if not trouve:
            raise KeyError
        
            
    def __delitem__(self, cle: C) -> NoneType:
        """ 
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)]) 
        $$$ del d1['a'] 
        $$$ d1 
        DicoTrie([Association("b", 2)]) 
        $$e del d1['c'] 
        KeyError 
        """
        res = []
        trouve = False
        for assos in self.liste_assos:
            if assos.cle ==cle:
                trouve = True
            else:
                res.append(assos)
        if not trouve:
            raise KeyError
        self.liste_assos  = res
    def __contains__(self, cle: C) -> bool:
        """ 
        $$$ d1 = DicoTrie([Association("a", 1), Association("b", 2)]) 
        $$$ 'a' in d1
        True
        $$$ 'c' in d1
        False
        """
        for assos in self.liste_assos:
            if assos.cle == cle:
                return True
        return False
if __name__ == '__main__':
    import apl1test
    apl1test.testmod('dicotrie.py')