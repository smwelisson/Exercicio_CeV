# from exerc107 import moeda
import moeda

# valor = float(input('Digite um valor: R$'))
valor = 423.00

print(f"O metade de {valor} é {moeda.metade(valor)}")
print(f"O dobro de {valor} é {moeda.dobro(valor)}")
print(f"O aumento de 10% é {moeda.aumento(valor, 10)}")
