"""programa que leia um numero n e mostre na tela os n primeiros elesmentos de uma sequencia de Fibonacci"""
#num: int = int(input("Digite o número para iniciar a seguencia de Fibonacci: "))
quant = int(input("O números de elementos da sequencia: "))
cont = 3
numi = 0
numf = 1
print("{} -> {} -> ".format(numi, numf), end="")
while cont <= quant:
    numt = (numi + numf)
    numi = numf
    numf = numt
    print("{} -> ".format(numt), end="")
    cont += 1

print("Fim")