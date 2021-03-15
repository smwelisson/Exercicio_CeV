#programa que leia nome e preço de varios produtos e se vai ou nao continuar.
#mostre: A) total gasto na compra  B)quantos produtos custam mais de 1.000,00  C) qual o nome do produto mais barato
print("=" * 15)
print("Lojão Baratissimo")
print("=" * 15)
cont_mil = soma = barato = cont = 0
nome_barato = ""
while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    cont += 1
    soma += preco
    if preco > 1000:
        cont_mil += 1
    if cont == 1 or preco < barato:
        barato = preco
        mais_barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break


print("-" * 10, "Fim do programa", "-" * 10)
print(f"A) O total da sua compra foi de R$ {soma}")
print(f"B) Existem {cont_mil} produtos estão acima de R$ 1.000,00")
print(f"C) O produto mais barato da sua compra foi o {mais_barato}")
