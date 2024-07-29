import random
numeros = [0,1,2,3,4,5]
escolhido = random.choice(numeros)
print('-=-' *18)
print('Irei pensar em um número entre 0 e 5, tente advinhar!')
print('-=-' *18)
numero = int(input('Escolha um número entre 0 e 5: '))
if numero == escolhido:
    print('YOU WIN! você acertou')
else:
    print('YOU LOSE! o computador venceu!')
    print('Eu escolhi o número {}'.format(escolhido))