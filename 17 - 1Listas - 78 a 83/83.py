lista = [input("Digite a expressão matématica para validar: ")]
print(lista)
esq = lista[0].count('(')
dir = lista[0].count(')')
print(esq, dir)
if esq == dir:
    print("Sua expressão está CORRETA")
else:
    print("Sua expressão está ERRADA")
