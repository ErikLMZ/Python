while True:
    try:
        operador = int(input('Digite o numero que deseja ver a tabuada: '))
        break
    except:
        print('Número Inválido, informe um número INTEIRO!')

inicio = 1
fim = 10
for num in range(inicio, fim+1):
    tabuada = num * operador
    print('{} x {} = {}'.format(num, operador, tabuada))