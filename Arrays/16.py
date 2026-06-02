vet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

n = len(vet)
#Construção
for i in range(n):    
    for j in range(i+1):
        #end=' ' para nao pular de linha
        print(vet[j], end=" ")
    print('')

#Desconstruçã
for i in range(n-1,0,-1):    
    for j in range(i+1):
        #end=' ' para nao pular de linha
        print(vet[j], end=" ")
    print('')