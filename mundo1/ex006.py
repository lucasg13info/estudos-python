# recebe um num e mostra o dobro, triplo e razq
import math

num = int(input("Entre com um número:\n"))

print('O número inserido foi {}, o dobro é {}, o triplo é {} e a raiz é {:.2f}'.format(num, (num*2), (num*3), (math.pow(num, 1/2))))
