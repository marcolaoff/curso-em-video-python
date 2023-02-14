'''a1 = int(input('Digite o ano para ver se ele é Bissexto ou não:'))
if a1 % 4 == 0:
    if a1 % 100 == 0 and a1 % 400 != 0 :
        print('O ano não é Bissexto!')
    else:
        print('O ano é Bissexto')
else:
    print('O ano não é Bissexto!')'''

from datetime import date
ano = int(input('Digite o ano que quer analisar! Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é Bissexto'.format(ano))
else:
    print('o ano {} não é Bissexto'.format(ano))