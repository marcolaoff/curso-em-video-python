real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 4.62
euro = real / 5
kwanza = real * 89.12
print('Com R${:.2f} você consegue comprar US$ {:.2f}, consegue comprar EUR {:.2f}, e consegue comprar AOA {:.2f}'.format(real,dolar,euro,kwanza))
