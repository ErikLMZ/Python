from datetime import datetime
ano = int(input('Informe seu ano de nascimento: '))
anoatual = datetime.now()
anoatualfinal = anoatual.year 
if anoatualfinal - ano == 18:
    print('Você deve se alistar esse ano!')
elif anoatualfinal - ano < 18:
    print('Você ainda não precisa de alistar!')
elif anoatualfinal - ano > 18:
    print('Seu tempo de alistamento já passou!')