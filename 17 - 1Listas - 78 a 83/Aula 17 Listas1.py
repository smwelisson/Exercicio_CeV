# Listas são mutaveis
num = [6, 2, 5, 9, 7]
print("A lista: ", num)
# Podemos trocar os elementos passando a posição:
num[1] = 3
print("Trocada o elemento 5 pelo 3: ", num)
# Acrecentar um novo elemento:
num.append(10)
print("Com mais um elemento: ", num)
# Colocar em ordem:
num.sort()
print("Ordem crescente: ", num)
num.sort(reverse=True)
print("Ordem decrescente: ", num)
# Para ver a quantidade de elementos
quantidade = len(num)
print("Quantidade de elementos:", quantidade)
print(f"Quantidade de elementos: {len(num)}")
# Para inserir elementos em determinadas posições. Primeiro a posição e depois o elemento:
num.insert(2, 0)
print("Adicionando o elemento 0 na posição 2: ", num)
# Para remover os elementos passando o indice: # sem indicie ele tira o ultimo
num.pop(2)
print("Removendo o 0", num)
# Para remover pelo elemento:
num.remove(5)
print("Removendo o elemento 5: ", num)
print("*" * 30)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print("Nova lista: ", valores)
print("Mostrando apenas os valores da lista:", end=" ")
for v in valores:
    print(v, end=" ")
print("")
# Para mostrar com os indices:
print("Mostrando apenas os valores da lista com seus indices:")
for i, v in enumerate(valores):
    print(i, v)
print("#" * 30)

# Para automatizar a inserção de elementos na lista
values = []
for add in range(0, 5):
    # add = int(input("Adicione um numero: "))
    values.append(int(input("Adicione um numero: ")))
print("Nova lista:", values)
# Na listas copiadas de outra listas, ganham ligações, ou seja, alterar uma muda em outra. para apenas copiar os elementos:
a = [1, 2, 3, 4]
b = a[:]
b[2] = 9
print("Lista A:", a)
print("Lista B:", b)












