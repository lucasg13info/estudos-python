#Número aleatorio entre 0 e 5, usuário deve tentar descobrir o número

from random import randint

adivinha = int(input('Tente adivinhar um número entre 0 e 5:  '))


valor = randint(0,5)


if adivinha == valor:
    print('Show, você acertou o número sorteado {}'.format(valor))
else:
    print('Você errou, o valor sorteado foi: {}'.format(valor))