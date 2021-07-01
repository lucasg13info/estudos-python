# INTERROMPENDO O WHILE


#1 
# cont = 1 

# while cont <= 10:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')

#2 
# n = cont = 0
# while cont < 3 : 
#     n = int(input('Leia um número: '))
#     cont += 1

#3 Break

n = s= 0
while True:
    n = int(input( 'Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}')