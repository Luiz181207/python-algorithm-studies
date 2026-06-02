print("Digite p para parar")

vetor = []

soma = 0
a = 0
while a < 1:
    n = input("Digite um numero:")
    if n == "p":
        print(vetor)
        a = 1
    else:
        n = int(n)
        vetor.append(n)

#Média:
for i in range(len(vetor)):
    soma += vetor[i]

media = soma / len(vetor)
print(f"A média dos {len(vetor)} números é: {media}")

#Desvio padrão:
sd = 0 #soma do desvio
for i in range(len(vetor)):
    sd += (vetor[i] - media) ** 2

md = sd / len(vetor)
dp = md ** 0.5
print(f"O desvio padrão é: {dp:.2f}")