def invert_ (vet):
    tev = []
    for i in range(len(vet) - 1 ,-1 ,-1): ##cuidado com o índice
        tev.append(vet[i])
    return tev

vet = [1,2,3,4,5,6,7,8,9,0]
print(invert_(vet))

"""
ou:
def invert_ (vet):
    tev = []
    for i in range(len(vet)):
        tev.insert(0, vet[i]) #.insert(posição, valor)
    return tev

vet = [1,2,3,4,5,6,7,8,9,0]
print(invert_(vet))
"""