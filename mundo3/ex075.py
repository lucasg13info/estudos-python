# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numer = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o ultimo número: ')))

print(f'Você digitou os valores {numer}')
print(f'O valor 9 apareceu {numer.count(9)} vezes')
if 3 in numer:
    print(f'O valor 3 apareceu na {numer.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados, foram: ')
for n in numer:
    if n % 2 ==0:
        print(n, end = ' ')