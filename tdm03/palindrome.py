#!/usr/bin/env python3


def est_palindromique(mot: str) -> bool:
    """Renvoie True ssi `mot` est palindromique.

    Précondition: \

    Exemples :

    $$$ est_palindromique('')
    True
    $$$ est_palindromique('A')
    True
    $$$ est_palindromique('RADAR')
    True
    $$$ est_palindromique('ABRACADABRA')
    False
    """
    return mot=='' or mot==mot[::-1] 

    

def en_palindrome(mot: str) -> tuple[int, str]:
    """Renvoie un couple n, pal_mot.

    - n est le nombre minimal d'insertions pour rendre mot palindromique ;
    - pal_mot est un palindrome obtenu après ces n insertions.

    précondition : \
    Exemples :
    $$$ en_palindrome('A')
    (0, 'A')
    $$$ en_palindrome('')
    (0, '')
    $$$ en_palindrome('RADAR')
    (0, 'RADAR')
    $$$ en_palindrome('ABRACADABRA')
    (4, 'ARBADRACARDABRA')
    """
    inverse=mot[::-1]
    res=''
    n=0
    for i in range(len(mot)):
        if mot[i]!=inverse[i]:
            n+=1
            res+=inverse[i]
        res+=mot[i]
    return (n,res)
            

if __name__ == '__main__':
    import l1test
    l1test.testmod('palindrome.py')

