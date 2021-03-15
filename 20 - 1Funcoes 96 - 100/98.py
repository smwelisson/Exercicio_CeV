def contador(i, f, p):
    for num in range(i, f+1, p):
        print(num, end=' ')


contador(1, 10, 1)
print("\n")
contador(10, -2, -2)
print("\n")
contador(1, 10, 3)
