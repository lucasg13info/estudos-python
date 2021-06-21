#Nomes aleatórios
# import random
#
# nome1 = (input('Informe o nome do primeiro participante: '))
# nome2 = (input('Informe o nome do segundo participante: '))
# nome3 = (input('Informe o nome do terceiro participante: '))
# nome4 = (input('Informe o nome do quarto participante: '))
#
# sorteio = nome1, nome2, nome3, nome4
#
# print('O nome escolhido foi {}'.format(random.randrange(sorteio)))
#


import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O aluno sorteado foi:', sorteio)