#Calculo IMC
altura = float(input( 'Informe sua altura em metros: '))
peso = float(input('Informe seu peso em Kg: '))


imc = peso / (altura ** 2) 

if imc <= 18.5: 
    print('Sua massa corporal é de: {:.2f}, você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Sua massa corporal é de: {:.2f}, você está no peso ideal'.format(imc))
elif imc <= 30:
    print('Sua massa corporal é de: {:.2f},você está com sobrepeso'.format(imc))
elif imc <= 40:
    print('Sua massa corporal é de: {:.2f}, você está com obesidade'.format(imc))
else:
    print('Sua massa corporal é de: {:.2f}, você está com obesidade móbida'.format(imc))