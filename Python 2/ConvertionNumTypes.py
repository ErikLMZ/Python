numero = int(input('Informe um número: '))
print('''Qual será o tipo de conversão:
[1] -Binário 
[2} -Octal 
[3] -Hexadecimal''')
tipo = str(input('')).strip().upper()
if tipo == "1":
    conversao = bin(numero)
    print('Seu número convertido para Binário fica: {}'.format(conversao))
elif tipo == "2":
    conversao = oct(numero)
    print('Seu número convertido para Octal fica: {}'.format(conversao))
elif tipo == "3":
    conversao = hex(numero)
    print('Seu número convertido para Hexadecimal fica: {}'.format(conversao))