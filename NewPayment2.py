salario = float(input('Informe seu salário: '))
if salario >= 1250:
    novosalario = (salario / 100) * 10 + salario
    print('Seu novo sálario é R$ {:.2f}'.format(novosalario))
else:
    novosalario = (salario / 100) * 15 + salario
    print('Seu novo salário é R$ {:.2f}'.format(novosalario))