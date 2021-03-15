"""programa pede 2 valores e mostra o seguinte menu:
1 somar
2 multiplicar
3 maior
4 novos numeros
5 sair do programa"""
entrada = 0
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
while entrada != 5:

    print('''>>>>>>>>>>Calculadora<<<<<<<<<<<
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')
    entrada = int(input("Sua opção? "))
    if entrada == 1:
        soma = n1 + n2
        print("A soma de {} e {} é igual a {}".format(n1, n2, soma))
    elif entrada == 2:
        multip = n1 * n2
        print("A multiplicação de {} e {} é igual a {}".format(n1, n2, multip))
    elif entrada == 3:
        if n1 > n2:
            maior = n1
            print("Entre {} e {} o maior é o {}".format(n1, n2, maior))
        else:
            maior = n2
            print("Entre {} e {} o maior é o {}".format(n1, n2, maior))
    elif entrada == 4:
        print("Digite os novos valores: ")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif entrada == 5:
        print("Fim do programa")
    print("=-" * 15)