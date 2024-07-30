import random
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i + 1]:
                #troca de elementos nas posições i e i + 1
                lista[i], lista[i+1] = lista[i+1], lista[1]


any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

inversed = [45,42,41,40,38,36,35,32,20,19,15,14,11,9,8,6,5,4,3,1]

repeated = [7,7,7,7,8,8,8,5,5,5,5,2,2,8,8,9,9,9,]

if __name__ == "__main__":
    lista = repeated
    print("\n Lista Desordenada: ")
    print(lista)
    bubble_sort(lista)
    print("\n Lista Ordenada: ")
    print(lista)
                
                
