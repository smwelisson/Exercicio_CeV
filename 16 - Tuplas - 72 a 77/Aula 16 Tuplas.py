# Tuplas são imutaveis, mas é possivel apaga-lás
# As tuplas ficam entre ( ) e cada um ganha um index, iniciando do 0
# Para chamar um elemento da tupla basta chamar a tupla junto com seu index entre [] -> nomeDaTupla[x]
# Dá para 'fatiar' as tuplas entre  os [] onde é possivel colocar até 3 direções, o inicio, o fim e o salto
tupla = [('a', 0), ('b', 1), ('c', 2)]
for l, n in tupla:
    print(l, n)


print("maximo", max(tupla))
print("minimo", min(tupla))
print("tamanho", len(tupla))
print("contagem", tupla.count(('a', 0)))
print("posição", tupla.index(('a', 0)))
