nom = str(input('Digite seu nome completo:'))
min = nom.lower()
mai = nom.upper()
noms = nom.split()
noms2 = noms[0]
noms3 = len(noms2)
print('Seu nome em letra minusculas é {}'.format(min))
print('Seu nome em letre maisculas é {}'.format(mai))
print('Seu primeiro tem {} letras'.format(noms3))