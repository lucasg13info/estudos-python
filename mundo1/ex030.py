#Par ou impar

valor = int(input('Digite um número: '))
resto = valor % 2
if resto == 0:
    print('Valor é par')

else:
    print('Valor impar')