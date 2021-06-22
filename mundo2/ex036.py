#Aprovação de imprestimo bancário

casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Em quanto tempo você quer pagar a casa? '))

prestacao = casa / (anos * 12)
minimo = salario * 30/100

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))


if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO!')

