metros = float(input('Digite um valor em metros:'))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
ml = metros * 1000
print('O valor informado em Km é {}km\nEm Hm é {}hm\nE em Dam é {}dam'.format(km,hm,dam))
print('O valor informado em dm é {}dm\nEm cm é {}cm\nE em mm é {}mm'.format(dm,cm,ml))