tamanho = float(input('Qual o tamanho da parede?'))
comprimento = float(input('Qual o comprimento da parede?'))
area = tamanho * comprimento
tinta = area / 2
print('Considerando que 1L de tinta é possivel pintar 2M², {}²m será necessário {} latas de tinta!'.format(area, tinta))