# Implementação do fatorial 

## Fatoral iterativo
''' python 
Exemplo:
def fatorial(n:int) -> int:
    ''' 
        algoritmo iterativo para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer > 0
        output:
            result - UM valor inteiro > 0
    '''
    res = 1
    for i in range(1, n+1):
        res *= i 
    return res '''

    ## Fatorial recursivo
    ''' python
    Exemplo:
    def fatorial_rec(n: int) -> int:
    ''' 
        algoritmo recursivo para resolver fatorial
        input:
            n:int - Um valor inteiro qualquer > 0
        output:
            result - UM valor inteiro > 0
    '''
    if(n <= 1):
        return 1
    else:
        return n * fatorial_rec(n-1)
    '''
