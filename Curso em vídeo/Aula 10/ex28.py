#import random
#lista = [0,1,2,3,4,5]
#n = random.choice(lista)
#print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
#print('Estou pensando em um número, tente advinha-ló')
#print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
#r = int(input('Digite o número que você acha que é:'))
#if r == n:
#    print('Parabéns você ganhou!')
#else:
#    print('Você perdeu tente outra vez :/')

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR" ou "Randomizar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # O jogador vai tentar adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Eita eu ganhei, eu pensei no número {} e não no número {}'.format(computador, jogador))

