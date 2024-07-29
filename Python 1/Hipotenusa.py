from math import hypot
catetoADJ = float(input('Informe o valor do cateto ADJ: '))
catetoOP = float(input('Informe o valor do cateto OP: '))
hipotenusa = hypot(catetoADJ, catetoOP)
print('A hipotenusa corresponde a: {:.2f}'.format(hipotenusa))
