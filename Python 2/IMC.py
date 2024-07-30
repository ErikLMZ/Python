from math import pow
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua Altura: '))
imc = peso / pow(altura)
print(imc)
if imc <= 18.5:
    print('Você está abaixo do seu peso ideal, seu imc é de {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal! seu imc é de {:.2f}'.format(imc))
elif 26 <= imc < 30:
    print('Você está com sobrepeso! seu imc é de {:.2f}'.format(imc))
elif 31 <= imc < 40:
    print('Você está obeso! seu imc é de {:.2f}'.format(imc))
elif imc > 40:
    print('Você está com obesidade morbida! seu imc é de {:.2f}'.format(imc))