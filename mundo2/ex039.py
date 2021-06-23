#Alistamento militar
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} '.format(ano))

else:
    saldo = idade - 18
    print('REFATARIO! Você ja deveria ter se alistado Há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} '.format(ano))
