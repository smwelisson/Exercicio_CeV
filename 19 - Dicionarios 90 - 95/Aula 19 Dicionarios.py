# print(filme)
# print(filme.values())
# print(filme.keys())
# print(dir(filme))

# filme = {'titulo': 'starwars', 'ano': 1977, 'diretor': 'George Lucas'}
# print(filme.items())
# print("")
# for keys, values in filme.items():
#     print(f"O {keys} é {values}")

# pessoas = {'nome': 'Well', 'sexo': 'M', 'idade': 28}
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# pessoas['nome'] = 'Cell'
# pessoas['novo item'] = 'um novo item'
# for k, v in pessoas.items():
#     print(f"{k} = {v}")

estado = dict()
brasil = list()
for cap in range(3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=" - ")
    print()

