import random

secreto = random.randint(1, 100)
chute = 0

while chute != secreto:
    chute = int(input("adivonha essa merda: "))

    if chute > secreto:
        print("mt em cima")
    elif chute < secreto:
        print("Mt em baixo")

print("Acertou!")
