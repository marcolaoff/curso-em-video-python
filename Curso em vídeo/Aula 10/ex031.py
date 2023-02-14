v1 = float(input('Digite a distância da viagem percorrida:'))
v2 = v1 * 0.50
if v1 > 200:
    v3 = v1 * 0.45
    print('Você ira ter de gastos R${:.2f}'.format(v3))
else:
    print('Você ira ter de gastos R${:.2f}'.format(v2))
print('Tenha uma boa viagem :D')