def maior(* lista):
    num = lista[0]
    o_maior = num
    for num in lista:
        if num > o_maior:
            o_maior = num
    print(o_maior)

maior(1, 2, 3, 40, 5)
maior(10, 2, 3, 4, 5)
maior(1, 2, 30, 4, 5)