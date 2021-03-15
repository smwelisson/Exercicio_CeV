'''Ler um numero inteiro qualquer e peça para o
usuario escolher qual será a base de conversão
1 para binario   2 para octal   3 para hexadecimal'''


numero = int(input("Digite um número: "))
base_conversao = int(input('''Qual a Base de conversão?

[ 1 ] Binário      [ 2 ] Octal      [ 3 ] Hexadecimal          

=>  '''))

if base_conversao == 1:
    print('[{}] Convertido para Binário é iqual a {}'.format(numero, bin(numero)[2:]))
elif base_conversao == 2:
    print('[{}] Convertido para Octal é iqual a {}'.format(numero, oct(numero)[2:]))
elif base_conversao == 3:
    print('[{}] Convertido para Hexadecimal é iqual a {}'.format(numero, hex(numero)[2:]))
else:
    print("ERROR")
