#Valor em metros convertido em centimetros e milimetro

valor = float(input('Qual o valor em metros? '))

cm = valor * 100
mm= valor * 1000

print('O valor inserido foi {} metros, é igual a {}cm e {}mm'.format(valor, cm ,mm))