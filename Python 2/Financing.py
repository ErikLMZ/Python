casa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe sua renda mensal: '))
anos = float(input('Informe quantos anos de parcelamento: '))

prestacao = casa / (anos * 12)
margem = (salario / 100) * 30

if prestacao > margem:
    print('Seu financiamento exede 30% do seu salário!')
else:
    print('PARABENS! Seu financiamento foi aprovado!!!')