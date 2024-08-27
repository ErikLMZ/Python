import time
import keyboard
print('Pressione qualquer tecla para iniciar a contagem regressiva.')
keyboard.wait('space') 


for contagem in range(10, 0, -1):
    print(contagem)
    time.sleep(1)

print('Feliz Ano Novo!!!')

