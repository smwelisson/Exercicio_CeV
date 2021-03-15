performace = dict()
goals = list()
performace['name'] = str(input("Soccer player: "))
matches = int(input(f"How many {performace['name']} matches did you play?: "))

for match in range(1, matches + 1):
    goals.append(int(input(f"How many goals in match {match}: ")))
performace['goals'] = goals[:]
performace['total'] = sum(goals)
print('-=' * 30)
print(performace)
print('-=' * 30)
for k, v in performace.items():
    print(f"O campo {k} tem o valor {v}")
print('-=' * 30)
print(f"The soccer player {performace['name']} play {matches} matches")
for i, v in enumerate(performace['goals']):
    print(f"   => In match {i+1} does {v} goals")
print(f"Total {performace['total']} goals")
print('-=' * 30)
