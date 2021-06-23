#Jokenpo
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print(''' Suas opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)

print('------------------------------------------------')
print('Computador jogou:  {}'.format(itens[computador]))
print('Jogador jogou:  {}'.format(itens[jogador]))
print('------------------------------------------------')

if computador == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')
    
    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('Opção inválida')


elif computador == 1:
    if jogador ==0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')
    
    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('Opção inválida')


elif computador == 2:
    if jogador ==0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')
    
    elif jogador == 2:
        print('EMPATE')

    else:
        print('Opção inválida')
