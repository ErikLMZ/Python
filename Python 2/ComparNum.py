numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro número: '))
if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
elif numero1 == numero2:
    print('Os dois números são iguais!')