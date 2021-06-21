#leia um numero inteiro e retorne a parte inteira

#############opção 1 ##################
# from math  import trunc
#
# num = float(input('Informe um número ponto flutuante: '))
# convertInt = trunc(num)
#
# print('O número inserido foi {}, a a parte inteira dele é: {}'.format(num, convertInt))


############## Opção 2 ######################
num = float(input('Informe um num ponto flutuante: '))
print('O valor digitado foi {} e a sua porção nteira é {}'.format(num, int(num)))