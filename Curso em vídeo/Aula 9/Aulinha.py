s1 = str(input('Digite seu sexo'))
while s1 not in 'Masculino''masculino''Feminino''feminino':
    print('Você digitou errado tente novamente')
else:
    print('Olá muito prazer seu sexo é {}'.format(s1))