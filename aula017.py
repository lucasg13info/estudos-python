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
