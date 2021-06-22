# Valocidade máxima 80km/h se passar será multado

velocidade = float(input('Qual sua velocidade nesse momento? '))


if velocidade > 80:
    multa = (velocidade -80)  * 7
    print('Você foi multado em R$ {} reais, a velocidadde máxima é de: 80Km/h'.format(multa))
else:
    print('Ok, você está dentro da velocidade permitida')