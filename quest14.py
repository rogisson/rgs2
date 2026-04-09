n = int(input("Digite um número: "))

if n % 2 == 0:
    print("É par")
    if n % 4 == 0:
        print("Também é múltiplo de 4")
else:
    print("É ímpar")
