#Leia o cumprimeito do cateto oporto e do cateto adjacente de um triangulo e mostr o cumprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))