#programa que leia a idade e o sexo de varias pessoas e perguntar se quer ou não continuar. no final mostrar:
#A)quantas pessoas tem 18+   B) quantos homens    C)quantas mulheres com menos de 20
print("-" * 15)
print("CADASTRAMENTO")
print("-" * 15)
cont_idade = cont_homem = cont_mulher = 0
while True:
    #nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ").upper().strip()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == "M":
        cont_homem += 1
    if sexo == "F" and idade < 20:
        cont_mulher += 1
    continuar = input("Deseja cadastrar novamente? ").upper().strip()[0]
    if continuar == "N":
        break
    print("-" * 15)
print(f"Mais de 18: {cont_idade}")
print(f"Homens: {cont_homem}")
print(f"Mulheres com menos de 20: {cont_mulher}")
