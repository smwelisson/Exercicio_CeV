from random import randint

sort = dict()

for player in range(1, 5):
    sort[f'player{player}'] = randint(1, 6)
print("Sorted Values: ")
for k, v in sort.items():
    print(f"    The {k} takes {v}")
print("Player's ranking: ")
for i, v in enumerate(sorted(sort.items(), key=lambda x: x[1], reverse=True)):
    print(f"    {i+1}º place: {v[0]} with {v[1]}")
