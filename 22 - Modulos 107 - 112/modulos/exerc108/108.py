from exerc108 import moeda

# valor = float(input('Digite um valor: R$'))
valor = 3.5


print(f"O metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
print(f"O aumento de 10% é {moeda.moeda(moeda.aumento(valor, 10))}")
