'''programa que le o ano de nascimento e informe se ele
ainda vai se alistar, se é hora de se alistar ou se ja passou o tempo de se alistar
e ainda mostra o tempo que falta para se aliastar ou do tempo que se passou do alistamento'''

'''ano = int(input("Digite o ano do seu nascimento: "))
if ano < 2018:
    print('Ainda faltam {} anos para você se alistar'.format(2018-ano))
elif ano > 2018:
    print('já passou {} ano do seu alistamento'.format(ano-2018))
else:
    print('Você deve se alistar este ano')'''



'''Eu deveria ter importado de um biblioteca o tempo e ter realizado com a idade e não com os anos'''


ano_nasc = int(input("Informe o seu ano de nascimento: "))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade == 18:
    print("Você tem {} anos! Você vai se alistar esse ano".format(idade))
elif idade > 18:
    tempo_passado = idade - 18
    print("Você tem {} anos!Já passou do seu tempo de se alistar! Você está atrasado a {} anos".format(idade, tempo_passado))
    print("Você deveria ter se alistado em {}".format(ano_atual - tempo_passado))
elif idade < 18 and idade > 0:
    tempo_restante = 18 - idade
    print("Você tem {} anos! Você ainda não precisa se alistar! Ainda faltam {} anos".format(idade, tempo_restante))
    print("Você vai se alistar em {}".format(ano_atual + tempo_restante))
else:
   print("Você ainda não nasceu!")