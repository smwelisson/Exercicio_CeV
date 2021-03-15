'''calcule o valor a ser pago por um produto considerando o preço normal e a condição de pagamento
a vista: dinheiro/cheque: 10% de desconto
a vista: cartão/; 5%
em 2x no cartão: preço normal
3x ou mais no cartão 20% de juro'''

preco = float(input('Digite o preço do produto: R$'))
#Dava pra fazer tudo abaixo usando ''' ''' (e não varios \n)
forma = int(input('Diga a forma de pagamento \n'
'[1] Pagamento a Vista em Dinheiro/Cheque \n'
'[2] Pagamento a Vista no Cartão \n'
'[3] Pagamento a Prazo em 2x no Cartão \n'
'[4] Pagamento a Prazo em 3x ou mais no Cartão \n'
'\n'
'Digite a forma de pagamento: '))

if forma == 1:
    print("Valor final: R${}".format(preco - (preco*(10/100))))
elif forma == 2:
    print('Valor final: R${}'.format(preco - (preco*(5/100))))
elif forma == 3:
    print('Valor final: R${}'.format(preco))
elif forma == 4:
    n = int(input('Quantos meses? '))
    print("Valor final: R${} e suas parcelas serão de R${}".format((preco + (preco*(20/100))),(preco + (preco*(20/100))) / n ))

#codigo pode ser simplificado



#PODE SER SIMPLIFICADO - Tem como colocar um print pegar varios if e elif

print(10*"=", "Lojas Shaolim do Sertão", 10*"=")
print("")
valor = float(input("Digite o valor do pagamento: R$"))
forma_pagamento = int(input('''[ 1 ] A vista (Especie)
[ 2 ] A vista (Cartão)
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão
Escolha a formar de pagamento: '''))
if forma_pagamento == 1:
    print("Seu pagamento de R${} sairá por R${}".format(valor, valor - (valor*10/100)))
elif forma_pagamento == 2:
    print("Seu pagamento de R${} sairá por R${}".format(valor, valor - (valor*5/100)))
elif forma_pagamento == 3:
    print("Seu pagamento é de R${} ".format(valor))
elif forma_pagamento == 4:
    parcela = int(input("Numeros de parcelas: "))
    print("Seu pagamento de R${} será parcelado em {}x de R${:.2f}".format(valor, parcela, (valor + (valor*20/100)) / parcela))
else:
    print("ERRO")