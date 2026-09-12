def max_ (vet):
    maior = 0
    for elemento in vet:
        if elemento > maior:
            maior = elemento
    return maior

vet = [8,9,0,2,0,4,3,7,5,6,1,5,8,3,6]

print(max_(vet))