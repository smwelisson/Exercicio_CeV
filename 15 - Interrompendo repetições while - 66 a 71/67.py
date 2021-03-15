#Faça a tabuada de varios numeros, um de cada vez, para cada valor que for dada a entrada. o programa para quando for um num negativo
num = 0
while True:
    num = int(input("Digite um numero para ver sua tabuada: "))
    multiplicador = 0
    if num < 0:
        break
    while multiplicador != 10:
        multiplicador += 1
        print(f"{multiplicador} X {num} = {multiplicador * num}")
    print("-=" * 6)
print("Fim")