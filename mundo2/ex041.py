from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu anod e nascimento: '))
idade = atual - nascimento

print('Sua idade é: {}'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIM')

elif idade <= 14:
    print('Sua categoria é: INFANTIL')

elif idade <= 19:
    print( 'Sua categoria é JUNIOR')

elif idade <= 25:
    print('Sua categoria é Sênior')

else:
    print('Sua categoria é MASTER')