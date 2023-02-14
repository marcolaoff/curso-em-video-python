alt = float(input('Digite a altura da sua parede'))
lar = float(input('DIgite a largura da sua parede'))
area = alt * lar
tinta = area / 2
print('A áreaa da sua parede é de {}m2\nPara pintar essa parede, você precisaria de {}l de tinta'.format(area,tinta))