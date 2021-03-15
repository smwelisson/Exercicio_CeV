'''Refaça o desafio 09, mostrando a tabuada de um numero que o usuario escolher, usando o laço for'''

tabuada = int(input("qual a tabuada você quer saber? "))
inicio = int(input("de onde ela deve começar? "))
fim = int(input("em qual número ela deve parar ?"))

for coluna in range(inicio, fim+1):
    print(tabuada, ' x ', coluna, ' = ', tabuada*coluna)
