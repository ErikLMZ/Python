ano = int(input('Informe seu ano de nascimento: '))
if 2024 - ano <= 9:
    print('sua categotia é: MIRIM')
elif 2024 - ano <= 14:
    print('sua categoria é: INFANTIL')
elif 2024 - ano <= 19:
    print('sua categoria é: JUNIOR')
elif 2024 - ano > 19:
    print('sua categoria é: MASTER')