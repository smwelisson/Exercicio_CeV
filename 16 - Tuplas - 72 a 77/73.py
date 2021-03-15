times = ("Corinthias", "Flamengo", "Botafogo", "Palmeiras", "Juventos", "Gremio", "Cruzeiro", "Chapecoense", "Piaui", "Fortaleza", "Santos")
print(times)
print(f"Os 5 primeiros times são: {times[0:5]}")
print(f"Os 4 ultimos times são: {times[-4:]}")
print(f"Os times em ordem alfabetica são: {sorted(times)}")
print(f"A Chapecoense está na {times.index('Chapecoense') + 1 }ª posição")


