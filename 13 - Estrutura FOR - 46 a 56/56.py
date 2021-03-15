'''programa que leia o nome, idade e sexo de 4 pessoas e mostre:
a media de idade do grupo;    o nome do homem mais velho;   quantas mulheres tem menos de 20 anos'''
media = 0
count = 0
maior = 0
nomemaisvelho = ""
for p in range(1,5):
    print("==== {}º Pessoa ====".format(p))
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (m ou f)): ")
    media += idade/4
    if sexo == 'f':
        if idade < 20:
            count += 1
    if sexo == 'm':
        if p == 1:
            maior = idade
            nomemaisvelho = nome
        else:
            if idade > maior:
                maior = idade
                nomemaisvelho = nome
print("_________________________________")
print("A média de idade do grupo é de {}".format(media))
print("O Homem mais velho tem {} anos e se chama {}".format(maior, nomemaisvelho))
print("Ao todo, ha {} mulheres com menos de 20 anos".format(count))
