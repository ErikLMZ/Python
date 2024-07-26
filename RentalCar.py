dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km foram rodados? '))
aluguel = dias * 60 + km * 0.15
print('O valor do alguel ficou em R$ {} por {} km rodados e {} dias alugados'.format(aluguel, km, dias))