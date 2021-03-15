list = []
pessoas = {}
quantidade = soma_idade = 0
while True:
    pessoas['name'] = str(input("Name: "))
    while True:
        pessoas['sexo'] = str(input("Sex[M/F]: ")).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print("ERRO. Tente novamente:")
    pessoas['age'] = int(input("Age: "))
    list.append(pessoas.copy())
    quantidade += 1
    while True:
        cont = str(input("Continue?[S/N]: ")).upper()[0]
        if cont in "SN":
            break
        print("Valor invalido")
    if cont in "N":
        break
listaMulheres = []
for n in range(len(list)):
    soma_idade += list[n]['age']
    if list[n]['sexo'] in 'Ff':
        listaMulheres.append(list[n]['name'])
media = soma_idade/quantidade

print('-=' * 30)
print("<< ENCERRADO >>")
print('-=' * 30)
print(list)
print('-=' * 30)
print(f"A) Ao todo temos {quantidade} pessoas cadastradas")
print(f"B) A média de idade é de {media:2} anos")
print(f"C) As mulheres cadastradas foram: {listaMulheres}")
acima_media = []
for n in range(len(list)):
    if list[n]['age'] > media:
        acima_media.append(list[n]['name'])
print(f"D) Lista das pessoas que estão acima da média: {acima_media}")
