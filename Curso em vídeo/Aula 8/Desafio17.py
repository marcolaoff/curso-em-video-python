'''import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacesnte:'))
ch = co ** 2 + ca ** 2
hp = math.sqrt(ch)
print('A hipotenusa vai merdir {:.2f}'.format(hp))'''

'''Outra forma muito mais simples'''

import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimenteo do cateto adjacente:'))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
