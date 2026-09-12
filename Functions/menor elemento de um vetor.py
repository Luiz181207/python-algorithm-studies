def min_ (vet):
    menor = vet[0]
    for elemento in vet:
        if elemento < menor:
            menor = elemento
    return menor

vet = [1,3,1,4,6,2,5,7,4,5,8,9,7,0]
print(min_(vet))