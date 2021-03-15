def fatoria(num=1, show='s'):
    f = 1
    for c in range(1, num+1):
        f *= c
    if show == 's':
        return f
    else:
        return "fim"

print(fatoria(5))
print(fatoria(4, 'n'))