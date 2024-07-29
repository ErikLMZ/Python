salario = float(input('Qual seu salário atual?'))
reajuste = (salario / 100) * 15
novosalario = salario + reajuste
print('Com o reajuste de 15%, seu novo salário será de R$ {}'.format(novosalario))