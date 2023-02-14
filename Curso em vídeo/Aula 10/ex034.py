'''print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
m1 = int(input('Digite a primeira medida:'))
m2 = int(input('Digite a segunda medida:'))
m3 = int(input('Digite a terceira medida:'))
if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    print('Essas medidas formam um triangulo!')
else:
    print('Essas medidas não formam um triângulo!')'''

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
