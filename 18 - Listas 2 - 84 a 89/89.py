notas = list()
while True:
    add_aluno = []
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    add_aluno.append(nome)
    add_aluno.append(n1)
    add_aluno.append(n2)
    notas.append(add_aluno)
    cont = input("Continuar? [S/N] ")
    if cont == "n":
        break
print(notas)
print("-=" * 30)
print("No. NOME     MÉDIA")
print("-" * 30)
for i, aluno in enumerate(notas):
    print(f"{i}    {aluno[0]}      {(aluno[1] + aluno[2]) / 2}")
print("-" * 30)

while True:
    parar = int(input("Motrar notas de qual aluno? (999 interrompe): "))
    if parar == 999:
        break
    if parar <= len(notas) -1:
        print(f"Notas de {notas[parar][0]} são {notas[parar][1:3]}")
    print("-" * 30)
