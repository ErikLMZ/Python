import statistics
import re

nome = []
idade = []
sexo = []

for _ in range(3):  
    while True:
        try:
            
            while True:
                n = str(input('Qual seu nome? ')).strip()
                if not n or not re.fullmatch(r'[A-Za-z\s]+', n):
                    print("O nome deve conter apenas letras e espaços.")
                else:
                    nome.append(n)
                    break 
            
           
            while True:
                try:
                    i = int(input('Qual sua idade? '))
                    if i < 0 or i > 100:
                        print("A idade deve ser um número inteiro entre 0 e 100.")
                    else:
                        idade.append(i)
                        break  
                except ValueError:
                    print("A idade deve ser um número inteiro válido.")
            
           
            while True:
                s = str(input('Qual seu sexo (M/F)? ')).strip().upper()
                if s not in ('M', 'F'):
                    print("Sexo deve ser 'M' ou 'F'.")
                else:
                    sexo.append(s)
                    break  

            break  

        except Exception as e:
            print(f'Erro inesperado: {e}. Por favor, insira os dados novamente.')


media = statistics.mean(idade)
print(f'A média das idades das pessoas informadas é {media:.2f}')
