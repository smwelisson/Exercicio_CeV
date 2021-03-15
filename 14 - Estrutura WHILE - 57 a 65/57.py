"""programa que leia o sexo de uma pessoa, mas só aceita os valores M e F. se estiver errado, pedir novamente
sexo = input("Digite seu sexo [M/F] para validar: ").strip().upper()
while sexo not in "MF":
    sexo = input('Digito invalido! Digite seu sexo [M/F] para validar: ').strip().upper()
print("Digito correto. Seu sexo é: {}".format(sexo))"""

resposta_esperada = input("Digite Sim, para parar o programa: ")
while resposta_esperada not in "Sim":
    resposta_esperada = input("Digite Sim, para parar o programa: ")
print("Fim do programa")