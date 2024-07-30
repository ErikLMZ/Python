numero = int(input('Informe um número: '))
tipo = str(input('Qual será o tipo de conversão, 1-Binário 2-Octal 3-Hexadecimal ? ')).strip().upper()
if tipo == "BINARIO":
    conversao = bin(numero)
    print('Seu número convertido para Binário fica: {}'.format(conversao))
elif tipo == "OCTAL":
    conversao = oct(numero)
    print('Seu número convertido para Octal fica: {}'.format(conversao))
else:
    conversao = hex(numero)
    print('Seu número convertido para Hexadecimal fica: {}'.format(conversao))