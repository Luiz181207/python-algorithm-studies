vet = [1, 2, 3, 4, 5, 6, 7, 8]

def triplo():
    n = int(input("digite um número"))
    n *= 3
    print(n)

def soma():
    n1 = int(input("digite:"))
    n2 = int(input("digite 2:"))
    n3 = int(input("digite 3:"))
    soma = n1 + n2 + n3
    print(soma)

def maxvet():
    max = vet[0]
    for i in range(len(vet)):
        if(vet[i] > max):
            max = vet[i]

    print(max)

maxvet()
