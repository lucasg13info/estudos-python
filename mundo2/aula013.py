#Laço de repetição - For

#1 = For simples
# for c in range (1,3):
#     print('Oi')


#2 = For de dois em dois ao contrário
# for i in range(6,0, 2):
#     print('OI', i)
# print('Fim')


#3 - For do maior par ao menor
# for i in range(6,0, -1):
#     print('OI', i)
# print('Fim')

#4 input do user
# n = int(input('Insira um número: '))
# for c in range(0, n):
#     print(c)
# print('FIM!')

#5 Input completo do user
# i = int(input('INICIO: '))
# f = int(input('FIM: '))
# p = int(input('PASSO: '))

# for c in range (i, f, p):
#     print(c)
# print('FIM!')

#6 
# for c in range(0,3):
#     n = int(input('Digite um valor: '))
#     m = n 
#     print(n)
# print('FIM!')

#7 Soma
s = 0
for c in range (0, 4):
    n = int(input('Digite um valor para somar: '))
    s += n
print('O valor da soma foi: {} '.format(s))