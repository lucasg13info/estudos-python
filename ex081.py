#Crie um programa que vai ler vários números e colocar em uma lista.        Depois disso, mostre:
#  A) Quantos números foram digitados.   
#  B) A lista de valores, ordenada de forma decrescente.                                                                                         
#  C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str (input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' *30)

print(f'Você digitou {len(valores)} numeros')