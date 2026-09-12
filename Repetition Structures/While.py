print(10 * '<', 'Média', 10 * '>')
print('Quando terminar digite 0 para finalizar')

soma = 0
contador = 0
n = 1

while(n != 0):
    num = float(input(f'Digite o {contador + 1}º número:'))

    contador = contador + 1
    soma = soma + num

    if num == 0:
        print('Calculando a média:')
        n = 0

contador = contador - 1
m = soma / contador

print(f'A média entre os {contador} números é:\n{m:.2f}')