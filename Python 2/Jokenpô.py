import random
def jokenpo():

    print('=-= JOKENPÔ =-=\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
    jogador = int(input('Faça sua jogada: '))
    escolhas = [1,2,3]
    computador = random.choice(escolhas)
    if jogador not in escolhas:
        print('Opção inválida, escolha novamente...')
        return True
    if jogador == 1 and computador == 2:
        print('YOU LOSE! o computador vencêu!')
        print('Eu escolhi {}'.format('PAPEL'))
    elif jogador == 1 and computador == 3:
        print('YOU WIN! jogador vencêu!')
        print('Eu escolhi {}'.format('TESOURA'))
    elif jogador == 2 and computador == 1:
        print('YOU WIN! jogador vencêu!')
        print('Eu escolhi {}'.format('PEDRA'))
    elif jogador == 2 and computador == 3:
        print('YOU LOSE! o computador vencêu!')
        print('Eu escolhi {}'.format('TESOURA'))
    elif jogador == 3 and computador == 1:
        print('YOU LOSE! o computador vencêu!')
        print('Eu escolhi {}'.format('PEDRA'))
    elif jogador == 3 and computador == 2:
        print('YOU WIN! jogador vencêu!')
        print('Eu escolhi {}'.format('PAPEL'))
    elif jogador == computador:
        print('PÔ! Empate, jogue novamente!')
        return True
    return False

while True:
    reiniciar = jokenpo()
    if not reiniciar:
        break