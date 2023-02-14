s1 = int(input('Digite o valor do salário para o reajuste:'))
if s1 <= 1250:
    s2 = s1 + (s1 * 0.15)
    print('O novo salário será R${:.2f}'.format(s2))
else:
    s3 = s1 + (s1 * 0.10)
    print('O novo salário será R${:.2f}'.format(s3))

'''salario = int(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f:'.format(salario,novo))'''


