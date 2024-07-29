numero1 = int(input('Fale um número?'))
numero2 = int(input('Fale mais um número?'))
operacao = input('Qual será a operação?')
resultado = 0
if operacao == '-':
    resultado = numero1 - numero2
if operacao == '+':
    resultado = numero1 + numero2
if operacao == '*':
    resultado = numero1 * numero2
if operacao == '/':
    resultado = numero1 / numero2
print('O resultado da operação é: {}'.format(resultado))