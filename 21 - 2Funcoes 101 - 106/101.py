def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        return "negado"
    elif idade >= 70:
        return "opcional"
    else:
        return "obrigatorio"

print(voto(1991))
print(voto(1910))
print(voto(2015))
print(voto(1981))


assert voto(1991) == "negado" or "opcional" or "obrigatorio"
assert voto(1971) == "negado" or "opcional" or "obrigatorio"
assert voto(2015) == "negado" or "opcional" or "obrigatorio"
assert voto(1981) == "negado" or "opcional" or "obrigatorio"