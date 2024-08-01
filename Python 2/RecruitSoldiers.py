from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
if  anoatual - ano == 18:
    print('Você deve se alistar esse ano!')
elif anoatual - ano < 18:
    print('Você ainda não precisa de alistar!')
elif anoatual - ano > 18:
    print('Seu tempo de alistamento já passou!')