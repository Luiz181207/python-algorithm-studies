"""Dado um vetor, crie um segundo vetor rotulando os indices do primeiro que contem valores acima (1) e abaixo da média
 (-1). Se caso for exatamente a média, então rotule como (0):

Ex: [30,10,40,50,20] --> média 30 -> [0,-1,1,1,-1]"""

print("Digite -1 para parar")

vet = []
a = 1

while a > 0:
    num = int(input("Digite um número: "))
    if num < 0:
        a = 0
    else:
        vet.append(num)

soma = 0
for i in range(len(vet)):
    soma += vet[i]

media = soma / len(vet)

print(vet)
print(f"Media == {media:.2f}")

for i in range(len(vet)):
    if vet[i] > media:
        vet[i] = 1
    elif vet[i] == media:
        vet[i] = 0
    elif vet[i] < media:
        vet[i] = -1

print(vet)