#Condicional

#1
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Seu carro é novinho, tem apenas {} ano'.format(tempo))
else:
    print('Poxa, seu carro já não é tão novo assim, tem {} anos.'.format(tempo))
print('FIM!')

#2
# tempo = int(input('Quantos anos tem o seu carro? '))
# print('Carro novo' if tempo<=3 else 'Carro Velho')

#3
# nome = str(input('Qual seu nome? '))
# if nome == 'Lucas':
#     print('Que nome top, {}! '.format(nome))
# else:
#     print('Seu nome é tão normal: {}'.format(nome))

#4
n1 = float(input('Informe sua nota 1: '))
n2 = float(input('Informe sua nota 2: '))
m = (n1 + n2) /2

if m >=6:
    print('Show, sua nota foi: {}, e você está aprovado!'.format(m))
else:
    print('Hmm, sua nota não foi boa, você tirou: {} e está de recuperação'.format(m))