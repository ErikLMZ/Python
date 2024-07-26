import math
ang = float(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
print('O angulo {} tem o seno de {:.2f}'.format(ang, seno))
coseno = math.cos(math.radians(ang))
print('O angulo {} tem o coseno de {:.2f}'.format(ang, coseno))
tangente = math.tan(math.radians(ang))
print('O angulo {} tem a tangente de {:.2f}'.format(ang, tangente))
