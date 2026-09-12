print(10 * '<', 'Tabuada', 10 * '>')

i = 1
n = int(input('Digite um número de 1 à 10:'))

while i <= 10:
    resultado = n * i
    print(f'{n} x {i} = {resultado}')
    i += 1
