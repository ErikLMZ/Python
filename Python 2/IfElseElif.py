nome = str(input('Qual é o seu nome ? ')).strip().upper()
if nome == 'GUSTAVO':
    print('Tenha um bom dia Gustavo!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == "PAULO":
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome não é muito comum!')