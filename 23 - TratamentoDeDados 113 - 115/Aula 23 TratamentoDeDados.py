try:
    a = int(input())
    b = int(input())
    r = a / b
except (ValueError, TypeError):
    print("Problema de tipos de dados")
except ZeroDivisionError:
    print("Não é possivel dividir por Zero")
except KeyboardInterrupt:
    print("Não tivemos dados informados")
except Exception as erro:             # Podem haver varios. Ocorre quando deu um tipo de problema
    print(f"Problema. {erro}")
else:                                 # Se não tiver erros
    print(r)
finally:                              # Ocorre sempre
    print("fim")
