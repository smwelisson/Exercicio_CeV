def notas(* notas, sit=False):
    boletim = {}
    media = float(f'{sum(notas) / len(notas):.2}')
    boletim['maior'] = max(notas)
    boletim['menor'] = min(notas)
    boletim['qtd'] = len(notas)
    boletim['media'] = media
    if sit == True:
        if media > 6:
            boletim['situacao'] = 'boa'
        else:
            boletim['situacao'] = 'ruim'
    return boletim

print(notas(5, 2, 3))
print(notas(5, 2, 3, sit=True))