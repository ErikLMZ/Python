km = float(input('Informe a distância do seu destino: '))
if km <= 200:
    passagem = km * 0.50
    print('Sua passagem é no valor de R$ {:.2f}'.format(passagem))
else:
    passagem = km * 0.45
    print('Sua passagem é valor de R$ {:.2f}'.format(passagem))
