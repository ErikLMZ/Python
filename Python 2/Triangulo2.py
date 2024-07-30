r1 = float(input('primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Análisando...')
if r1 == r2 == r3:
    print('Este trinânglo é Equilátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Este trinângulo é Isósceles')
else:
    print('Este trinângulo é escaleno')