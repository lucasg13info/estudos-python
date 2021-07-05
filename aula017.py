#Listas
##Ordenação de valores do menor para o maior
# valores = [8, 2, 5, 4 , 9 , 3, 0]
# valores.sort()
# print(valores)


##Ordenação de valores do maior para o menor
# valores = [8, 2, 5, 4 , 9 , 3, 0]
# valores.sort(reverse=True)
# print(valores)

##Quantos valores existentes?
# valores = [8, 2, 5, 4 , 9 , 3, 0]
# print(len(valores))

#MÉTODOS QUE PODEM SER UTILIZADOS NA LISTA
num = [2, 5, 9 ,1] # Definindo a lista
num[2] = 3 #Alterando o valor da posição 2
num.append(7) #Adicionando o valor 7 no final
num.sort() #Ordena em ordem crescente
num.sort(reverse=True) #Ordena em ordem decrescente
num.insert(2, 0) # Adiciona o valor zero na posição 2
num.pop() #Elimina o ultimo valor da lista
num.pop(2) #Elimina o valor na posição 2 da lista
num.remove(2) #Elimina o elemento 2
print(f'Essa lista tem {len(num)} elementos') # Lista a quantidade de elementos

print(num)


#remove o num 5 se ele existir na lista
num2 = [0, 4, 5]
if 5 in num2:
    num2.remove(5)
else:
    print('Não achei o número 5')
print(num2)



#Adicionando valores de entrada em lista
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')


#Cópia de listas:
a = [2,3,4,5,6,]
b = a[:] #Copia todos elmentos de a
print(f'Lista A: {a}')
print(f'Lista B: {b}')