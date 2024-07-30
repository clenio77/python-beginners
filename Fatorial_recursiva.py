#Python (Fatorial usando recursão):
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print("O Fatorial de 5 =", resultado)  # Output: 5! = 120

print('='*40)

#Python(fatorial sem usar recursão):

def fatorial_sem_recursao(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 5
resultado = fatorial_sem_recursao(numero)
print(f'O fatorial de {numero} é: {resultado}')  # Saída: O fatorial de 5 é: 120
