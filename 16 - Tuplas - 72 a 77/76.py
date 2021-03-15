compras = (('Lápis', 1.75), ('Borracha', 2.00), ('Caderno', 15.00), ('Estojo', 25.00), ('Transferidor', 4.20),
           ('Compasso', 9.99), ('Mochila', 120.32), ('Canetas', 22.30), ('Livro', 35.90))
for item, preco in compras:
    print(f"{item:.<20} R$ {preco}")