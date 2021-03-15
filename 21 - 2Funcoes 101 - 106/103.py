def ficha(nome='desconhecido', gols='0'):
    return (f'O jogador {nome} marcou {gols} gols')


print(ficha(nome='rell', gols='5'))
print(ficha(gols='5'))
print(ficha(nome='rell'))
