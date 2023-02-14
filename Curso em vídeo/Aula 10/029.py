print('Bom Dia, Diriga com segurança!')
vl = float(input('Digite a velocidade em que o carro passou:'))
if vl > 80:
    print('Você foi multado!!!')
    multa = (vl-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('O carro passou com a velocidade permitida :D')
