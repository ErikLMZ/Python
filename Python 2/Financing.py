casa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe sua renda mensal: '))
tempo = float(input('Informe o tempo de parcelamento: '))

prestacao = casa / tempo
margem = (salario / 100) * 30

if prestacao > margem:
    print('Seu financiamento exede 30% do seu salário!')
else:
    print('PARABENS! Seu financiamento foi aprovado!!!')