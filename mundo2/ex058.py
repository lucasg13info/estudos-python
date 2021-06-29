#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Sou seu pc e acabei de pensar em um numero entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... tente outra vez')
        elif jogador > computador:
            print('Menos ... tente outra vez')
print('Acertou com {} palpites'.format(palpites))
