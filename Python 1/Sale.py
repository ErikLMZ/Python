preco = float(input('Qual o valor do produto?'))
desconto = (preco / 100) * 5
novopreco = preco - desconto
print('Este produto está com o desconto de 5%, saindo de {} por {}!'.format(preco, novopreco)) 