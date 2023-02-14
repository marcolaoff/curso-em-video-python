d1 = float(input('Informe a quantidade de dias alugados?'))
ttl = float(input('Informe o total de Km rodados?'))
d2 = d1 * 60
ttl1 = ttl * 0.15
tg = d2 + ttl1
print('O total a pagar é de R${}'.format(tg))