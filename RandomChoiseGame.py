import random
numeros = [0,1,2,3,4,5]
escolhido = random.choice(numeros)
print('Advinhe o número')
numero = int(input('Escolha um número entre 0 e 5: '))
if numero == escolhido:
    print('YOU WIN! você acertou')
else:
    print('YOU LOSE! o computador venceu!')
    print('Eu escolhi o número {}'.format(escolhido))