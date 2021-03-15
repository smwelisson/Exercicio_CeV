def funcao_geradora():
    yield 1
    yield 2

gerador = funcao_geradora()

# for valor in gerador:
#     print(valor)

#  1

print(next(gerador))
print(next(gerador))
print(next(gerador))

