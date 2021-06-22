#Leia um angulo e retorno o seno, cosseno e tangente
import math
angulo = float(input('Informe o angulo: '))


print('O valor do Seno é:  {:.2f}'.format(math.sin(math.radians(angulo))))
print('O valor do Cosseno é:  {:.2f}'.format(math.cos(math.radians(angulo))))
print('O valor da Tangente é:  {:.2f}'.format(math.tan(math.radians(angulo))))