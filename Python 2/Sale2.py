valor = float(input('valor do produto: '))
print('Informe o método de pagamento: ')
print('1 - A vista (dinheiro/cheque)')
print('2 - A vista (cartão)')
print('3 - 2x no cartão (crédito)')
print('4 - 3x ou mais no cartão (parcelado)')
print('Informe uma das 4 opçõess')
forma = str(input('')).strip().upper()
if 'DINHEIRO' in forma or 'CHEQUE' in forma or '1' in forma:
    desconto = (valor / 100) * 10
    novovalor = valor - desconto
    print('Valor total com 10% de desconto: R${:.2f}'.format(novovalor))
elif 'CARTÃO' in forma or '2' in forma:
    desconto = (valor / 100) * 5
    novovalor = valor - desconto
    print('Valor toral com 5% de desconto: R${:.2f}'.format(novovalor))
elif 'CRÉDITO' in forma or '3' in forma:
    print('O valor total: R${:.2f}'.format(valor))
elif 'PARCELADO' in forma or '4' in forma:
    taxa = (valor / 100) * 20
    novovalor = valor + taxa
    print('O valor total: R${:.2f}'.format(novovalor))