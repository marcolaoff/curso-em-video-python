import math
ag = float(input('Digite o valor do ângulo:'))
seno = math.sin(math.radians(ag))
print('O angulo de {} tem o Seno de {:.2f}'.format(ag,seno))
cos = math.cos(math.radians(ag))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(ag,cos))
tan = math.tan(math.radians(ag))
print('O angulo de {} tem a tangente de {:.2f}'.format(ag,tan))
