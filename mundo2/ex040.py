#Média do aluno

n1 = float(input('Informe sua nota na prova 1: '))
n2 = float(input('Informe sua nota na prova 2: '))

media = (n1 + n2) / 2


if media <=5:
    print('REPROVADO')
elif media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
