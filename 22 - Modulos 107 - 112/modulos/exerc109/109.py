from exerc109 import moeda

valor = 10  # valor = float(input('Digite um valor: R$'))

print(f"O metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}")
print(f"O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}")
print(f"O aumento de 10% é {moeda.aumento(valor, form=True)}")
