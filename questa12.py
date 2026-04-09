idade = int(input("Digite a idade: "))

if idade <= 12:
    print("bebe")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("velho")
