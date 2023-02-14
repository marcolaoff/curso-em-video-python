sx = str(input('Digite seu sexo:')).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input('Dados inválido. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sx))
