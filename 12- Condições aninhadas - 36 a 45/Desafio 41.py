'''leia o ano de nascimento e diga a categoria
até 9 mirim, até 14 infantil, até 19 junior, até 20: senior, acima de 20 master'''

ano = int(input('Digite o seu ano de nascimento: '))
i = 2018 - ano

if i <= 9:
    print("Você tem {} anos e está na categoria Mirin".format(i))
elif i > 9 and i <=14:
    print("Você tem {} anos e está na categoria Infantil".format(i))
elif i >= 14 and i < 19:
    print("Você tem {} anos e está na categoria Junior".format(i))
elif i >= 19 and i < 20:
    print("Você tem {} anos e está na categoria Senior".format(i))
elif i > 20:
    print("Você tem {} anos e está na categoria Master".format(i))


#pode ser simplificado

from datetime import date
ano_atual = date.today().year
nasc = int(input("Diga o ano que você nasceu: "))
idade = ano_atual - nasc
print("Você nasceu em {}, logo possui {} anos".format(nasc, idade))
if idade > 25:
    print("Você está na categoria MASTER")
elif 25 >= idade > 19:
    print("Você está na categoria SENIOR")
elif 19 >= idade >= 15:
    print("Você está na categoria JUNIOR")
elif 15 > idade >= 10:
    print("Você está na categoria INFANTIL")
elif 9 > idade > 0:
    print("Você está na categoria MIRIM")
else:
    print("Você não nasceu ainda.")