incio = 3
fim = 500
passo = 3
soma = 0
for num in range(incio, fim, passo):
    print(num)
    soma += num

print('a soma total é de {}'.format(soma))