'''Leia o peso e altura e calcule o IMC e mostre
menos que 18,5: abaixo do peso
18,5 e 25 peso ideal
entre 25 e 30: sobrepeso
entre 30 e 40 obesidade
acima de 40: obesidade morbida'''

a = float(input('Digite sua Altura: '))
p = float(input('Digite seu Peso: '))
imc = p / (a ** 2)
print("O seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc < 40:            # 30 <= imc < 40
    print('Você está com Obesidade')
elif imc >= 40:
    print('Você está com Obesidade Morbida')

altura = float(input("Digite sua Altura em metros: "))
peso = float(input("Digite o seu Peso em kg: "))
imc = peso / (altura**2)
print("Seu imc é de {:.2f}, você está ".format(imc), end=(""))
if imc < 18.5:
    print("abaixo do peso.")
elif imc < 25:
    print("no peso ideal.")
elif imc < 30:
    print("com sobrepeso.")
elif imc < 40:
    print("com obesidade.")
elif imc > 40:
    print("com obesidade morbida")
else:
    print("Você está morto.")