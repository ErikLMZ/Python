nota1 = float(input('Informe sua nota do 1° Semestre: '))
nota2 = float(input('Informe sua nota do 2° Semestre: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO!')
elif media == 5 or media < 6.9:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')