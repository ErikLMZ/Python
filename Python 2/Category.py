from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
if anoatual - ano <= 9:
    print('sua categotia é: MIRIM')
elif anoatual - ano <= 14:
    print('sua categoria é: INFANTIL')
elif anoatual - ano <= 19:
    print('sua categoria é: JUNIOR')
elif anoatual - ano > 19:
    print('sua categoria é: MASTER')