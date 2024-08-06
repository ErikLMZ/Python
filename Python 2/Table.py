operador = int(input('Digite o numero que deseja ver a tabuada: '))
inicio = 1
fim = 10
for num in range(inicio, fim+1):
    tabuada = num * operador
    print('{} x {} = {}'.format(num, operador, tabuada))