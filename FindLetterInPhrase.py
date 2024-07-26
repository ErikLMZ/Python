frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparece {} vezes!'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece a ultima vez na posiçãoição {}'.format(frase.rfind('A')+1))