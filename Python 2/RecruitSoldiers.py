ano = int(input('Informe seu ano de nascimento: '))
if 2024 - ano == 18:
    print('Você deve se alistar esse ano!')
elif 2024 - ano < 18:
    print('Você ainda não precisa de alistar!')
elif 2024 - ano > 18:
    print('Seu tempo de alistamento já passou!')