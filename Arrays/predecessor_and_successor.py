"""Para cada posição [i] do vetor, imprima o valor atual, seu antecessor e sucessor"""

vet = [1,2,3,4,5,6,7,8,9,]

for i in range(0,len(vet)):
    print(30 * "=")
    print(f"Antecessor: {vet[i-1]}\n"
          f"Número: {i}\n"
          f"Sucessor: {i+1}")
