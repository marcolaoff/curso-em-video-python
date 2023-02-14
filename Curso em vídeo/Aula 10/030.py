n1 = int(input('Digite um número para verificar se ele é impar ou par'))
n2 = n1 % 2
if n2 == 0:
    print('O número {} é par'.format(n1))
else:
    print('o número {} é impar'.format(n1))