from ap_decorators import trace,count
@count
def fibo(entier:int)->int:
    """ 
    Précondition : 
    Exemple(s) :
    $$$ fibo(10)
    55
    """
    if entier==0:
        return 0
    elif entier==1:
        return 1
    else:
        return fibo(entier-1)+fibo(entier-2)
    
def coefficient_bino(n:int,p:int):
    """ calcule les coefficients  binomiaux

    Précondition : n>p>0
    Exemple(s) :
    $$$ coefficient_bino(5,4)
    5
    """
    if  p==0 or p==n:
        return 1
    else:
        return coefficient_bino(n-1,p-1)+coefficient_bino(n-1,p)
    
