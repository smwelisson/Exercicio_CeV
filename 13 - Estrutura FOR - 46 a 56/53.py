'''leia uma frase qualquer e diga se é um palindromo, desconconsiderando os espaços'''
frase = input("Digite uma frase ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
#inverso = junto[::-1] outra forma de fazer a questão sem o for. isso indica que vai escrever "junto" de tras pra frente
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print("É um palindromo")
else:
    print("Não é palindromo")

# o "len(junto)" contou quantas letras tinha na frase. o "len(junto)-1" indica que é pra começar da ultima
# o segundo "-1" indica onde vai parar, ou seja vai parar a contagem no "0"
# o terceiro -1 indica que é para mostrar de tras pra frente