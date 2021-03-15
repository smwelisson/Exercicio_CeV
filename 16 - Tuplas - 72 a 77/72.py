'''Programa que tenha uma tupla com os numeros de 0 a 20 por extenso
e receba um numero nesse intervalo e mostra-lo por extenso'''

n_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinto', 'seis', 'sete', 'oito', 'nove', 'dez',
              "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(n_extensos[num])
    else:
        break





