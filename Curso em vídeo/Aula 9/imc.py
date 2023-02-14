print('Calcular IMC')

alt = float(input('Digite sua altura'))
peso = float(input('Digite seu peso'))
imc = peso /(alt ** 2 )

if imc < 18.5:
    print('O seu imc está abaixo do normal')
elif imc <= 24.9:
    print('O seu imc está normal')
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 34.9:
    print('Você está com Obesidade I')
elif imc <= 39.9:
    print('Você está com Obesidade II')
else:
    print('Você está FUDIDO(você está com Obesidade III)')

print(imc)