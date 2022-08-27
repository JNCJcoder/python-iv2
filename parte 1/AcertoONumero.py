import random

def AcerteONumero():
    escolha = int(input("Escolha um número de 1 a 10: "))

    if escolha >= 1 and escolha <= 10:
        escolhaDoComputador = random.randint(1,3)

        if escolhaDoComputador == escolha:
            print("Parabéns! Você acertou o número escolhido :)")
        else:
            print("Poxa que pena, você não acertou. O número escolhido foi: ", escolhaDoComputador)
    else:
        print("Número inválido.")
        AcerteONumero()

AcerteONumero()