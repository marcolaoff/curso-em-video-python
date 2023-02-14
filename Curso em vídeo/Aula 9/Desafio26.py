lt = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes'.format(lt.count('A')))
print('A primeira letra apareceu na posição {} vezes'.format(lt.find('A')+1))
print('A última letra A apareceu na posição {}'.format(lt.rfind('A')+1))

