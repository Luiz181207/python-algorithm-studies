n = int(input('Digite um número:'))
soma = 0


while n > 10:
    soma += n % 10
    n = n // 10


soma += n
print(soma)
