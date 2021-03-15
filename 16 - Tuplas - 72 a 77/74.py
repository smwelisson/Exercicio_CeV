from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for num in n:
    print(num, end=",")
print()
print(f"O numero mais alto foi o {max(n)}")
print(f"O numero mais baixo foi o {min(n)}")


