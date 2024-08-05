import time 

iniciar = str(input('Iniciar a contagem regressiva? ')).strip().upper()
if iniciar == 'SIM':
    for contagem in range(10, 0, -1):
        print(contagem)
        time.sleep(1)
print('Feliz Ano Novo!!!')
