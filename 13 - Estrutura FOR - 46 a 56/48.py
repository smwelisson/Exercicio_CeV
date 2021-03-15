'''Faça um programa que calcule a soma entre os numeros impares que são multiplos de 3 no intervalo de 1 e 500  (87nºs = 20667)'''
somatorio = 0
cont = 0  #Pra cada vez que ele repetir o laço, ele vai somar mais um
for mult3 in range(0, 501, 3):
    if mult3 % 2 != 0:
        print(mult3, end=" ")
        somatorio += mult3 #somatorio = somatorio + mult3
        cont += 1 #cont = cont + 1
print(" ")

print("A soma de todos os {} numeros impares entre 1 e 500 é de {}".format(cont, somatorio))
