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
    return res 
    
try:
    n = int(input("Digite um número inteiro: "))
    print(f'O fatorial desse número é: {fatorial(n)}')
except ValueError:
    print("Entrada inválida! Isso não é um número inteiro.")