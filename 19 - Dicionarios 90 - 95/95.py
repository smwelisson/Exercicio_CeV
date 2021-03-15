players = []
while True:
    goals = []
    performace = {}
    performace['name_player'] = input("Player name: ")
    performace['matchs'] = int(input("Matches: "))
    for match in range(1, performace['matchs'] + 1):
        goals.append(int(input(f"How many goals in match {match}: ")))
    cont = input("Deseja continuar: [s/n]: ").lower()
    performace['qtd_goal'] = goals
    players.append(performace)
    if cont == 'n':
        break
# performace = {'name_player': 'vell', 'matchs': 3, 'qtd_goal': [1, 2, 1]}
# players = [{'name_player': 'vell', 'matchs': 3, 'qtd_goal': [1, 2, 1]}, {'name_player': 'zell', 'matchs': 1, 'qtd_goal': [0]}]
print(players)
print('-=' * 30)
print("Indice - Name         Matches      Scores      Total Scores")
for ind, val in enumerate(players):
        print(f"{ind} - {val['name_player']}    {val['matchs']}    {val['qtd_goal']}      {sum(val['qtd_goal'])}")
print('-=' * 30)
choice = int(input("Show information's player (999 to stop)"))
# choice = 0
if choice <= len(players):
        # print(f"{players[choice]['qtd_goal']}")
        for i, g in enumerate(players[choice]['qtd_goal']):
            print(f"No jogo {i} fez {g} gols")
else:
    print("Error")

# for k, v in performace.items():
#     print(f"O campo {k} tem o valor {v}")
# print(f"The soccer player {performace['name']} play {match} matches")

# for i, v in enumerate(performace['goals']):
#     print(f"   => In match {i+1} does {v} goals")
# print(f"Total {performace['total']} goals")
# print('-=' * 30)
