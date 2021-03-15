# galera = [['João', 19], ['Joaquim', 13], ['Ana', 33], ['Maria', 45]]
# for pessoa in galera:
#     print(pessoa[0], 'tem', pessoa[1], 'anos')


galera = []
dado = []
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
