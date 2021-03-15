'''leia o ano de nascimento de sete pessoas e mostre quantas ja atingiram a maioridade e quantas ainda não'''
from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input("Digite o {}º ano de nascimento: ".format(i)))
    idade = ano_atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print("existem {} pessoas MAIOR de idade e {} pessoas MENOR de idade".format(count1, count2))
