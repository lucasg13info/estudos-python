# Pergunte a distancia e cobre 0,50 até 200km e 0,45 para viagem mais longa

distancia = float(input('Qual a distancia da sua viagem em Km? '))

if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da sua viagem é de: R$ {} reais'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da sua viagem é de: R$ {} reais'.format(preco))

print('Boa viagem!')