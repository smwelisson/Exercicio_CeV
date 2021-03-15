'''ler 3 retas e dizer se pode formar um triangulo
se sim dizer se é equilatero(lados iguais)
isoceles(dois lados iguais
escaleno(todos os lados diferentes)'''

a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if a + b > c and a + c > b and c + b > a:
    print("Com essas retas é possivel fazer um triangulo")
    if a == b == c:
        print("Este é um triangulo EQUILATERO")
    elif a != b != c != a:
        print("Este é um triangulo ESCALENO")
    else:
        print("Este e´um triangulo ISOCELES")

else:
    print("Não é possível fazer um triangulo com essas medidas")


r1 = int(input("Digite a medida do primeiro lado: "))
r2 = int(input("Digite a medida do segundo lado: "))
r3 = int(input("Digite a medida do terceiro lado: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível fazer um triangulo com essas retas.")
    if r1 == r2 == r3:
        print("O triangulo sera equilatero.")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("O triangulo será isoceles.")
    elif r1 != r2 != r3 != r1:
        print("O triangulo será escaleno.")
else:
    print("Não é possivel fazer um triangulo com essas retas.")