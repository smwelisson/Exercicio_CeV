'''Calcule  duas notas e diga pela medio se esta aprovado, recuperação ou aprovado'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
if m >= 7:
    print("Você tem média {:.1f}. Você está APROVADO".format(m))
elif m < 5:
    print("VocÊ tem média {:.1f}. Você está REPROVADO".format(m))
elif m >= 5 and m <7:
    print("Você tem média {:.1f}. Você está de RECUPERAÇÂO".format(m))