#Calcule a área e quantidade de tinta para pintar (cada lata de tinha pinta 2m)

altura = float(input('Qual a altura da sua parede? '))
largura = float(input('Qual é a largura da sua parete? '))

area = altura * largura
tinta = (area / 2)

print('O valor de altura {} e largura da parede são {},a área equivale á {}m.'.format(altura, largura, area))
print('Contando que a tinha rende 2 metros, compre {}l de tintas'.format(tinta))