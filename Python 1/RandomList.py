import random
aluno1 = str(input('Qual o nome do primeiro aluno?'))
aluno2 = str(input('Qual o nome do segundo aluno?'))
aluno3 = str(input('Qual o nome do terceiro aluno?'))
aluno4 = str(input('Qual o nome do quarto aluno?'))
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
sequencia = random.shuffle(listaAlunos)
print('A sequência de apresentação é :')
print(listaAlunos)
