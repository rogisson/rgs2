amigos = input("Tem amigos? (s/n): ")
sol = input("Está fazendo sol? (s/n): ")
dinheiro = input("Tem grana? (s/n): ")

if amigos == "s" and (sol == "s" or dinheiro == "s"):
    print("Pode ir à praia parabens")
else:
    print("Não pode ir otario")
