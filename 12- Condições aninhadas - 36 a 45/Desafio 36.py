'''O programa pergunta o valor da casa, o salario e quantos anos ele vai pagar
Calcule o valor mensal, sabendo que ele
nao pode exceder 30% do salario ou então o emprestimo sera negado'''

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
tempo_quitacao = int(input("Em quantos anos você planeja pagar? "))
mensalidade = valor_casa / (tempo_quitacao*12)
limite_salario = salario * 30 / 100
if mensalidade <= limite_salario:
    print("Empréstimo aprovado! Sua mensalidade é de R${:.2f}".format(mensalidade))
else:
    print("Empréstimo negado!")
