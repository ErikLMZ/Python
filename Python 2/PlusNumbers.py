inicio = 1
fim = 6
entradas = [] 

for numeros in range(inicio, fim + 1):
    while True:
        entrada = input('Informe um número: ').strip()
        try:
            num = int(entrada)
            entradas.append(num)  # Adiciona o número à lista
            break 
        except ValueError:
            print("Entrada inválida. Por favor, informe um número inteiro.")

somapares = sum(num for num in entradas if num % 2 == 0)
print("A soma dos resultados pares é: {}".format(somapares))
