def leiaInt(msg):
    valido = False
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro! Tente novamente")
            continue
        except (KeyboardInterrupt):
            print("\nPrograma encerrado")
            return 0
        else:
            return n

n = leiaInt('Digite um valor: ')
print(f"O número digitado foi: {n}")
