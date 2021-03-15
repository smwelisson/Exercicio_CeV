palavra = ("aprender", "cegonha")
for p in palavra:
    print(f"\nNa palavra {p.upper()} temos as vogais: ", end=" ")
    for letra in p:
        if letra in "aeiou":
            print(f"{letra.lower()} ", end = "")

