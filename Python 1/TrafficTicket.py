velocidade = int(input('Informe a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Sua multa é de R${:.2f} reais'.format(multa))
else:
    print('Você não foi multado!')