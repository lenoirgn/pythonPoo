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
    $$$ est_palindromique('ARBADRACARDABRA')
    True 
    $$$ est_palindromique('ARBBRADCACDARBBRA')
    True
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
    $$$ en_palindrome('AB')
    (1, 'BAB')
    """
    if len(mot)<=1 or est_palindromique(mot):
        return (0,mot)
    elif  mot[0] == mot[-1]:
        n, pal = en_palindrome(mot[1:-1])
        return (n, mot[0] + pal + mot[-1])
        return (0,mot)
    else:
        # ajout au Debut
        n1, pal1 = en_palindrome(mot[1:])
        pal1 = mot[0] + pal1 + mot[0]
        # ajout a la fin 
        n2, pal2 = en_palindrome(mot[:-1])
        pal2 = mot[-1] + pal2 + mot[-1]
        if n2 <= n1:
            return (n2+1, pal2)
        else:
            return (n1+1, pal1)


            

if __name__ == '__main__':
    import l1test
    l1test.testmod('palindrome.py')

