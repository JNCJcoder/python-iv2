import random

palavras = ["arroz", "pato", "avestruz"]
letras = "" 
maximoDeErros = 3
erros = 0
palavraEscolhida = random.choice(palavras)

while erros < maximoDeErros:
    letraOculta = [letra if letra in letras else "_" for letra in palavraEscolhida]

    if not "_" in letraOculta:
        print("Parabéns você venceu! A palavra é: ", "".join(letraOculta))
        break

    print("".join(letraOculta))
    print("Vidas: ", maximoDeErros - erros)

    entrada = input("Digite uma letra: ")
    if len(entrada) == 1:
        if entrada in palavraEscolhida:
            letras += entrada
        else:
            print("A letra escolhida não está presente na palavra. Você perdeu uma vida.")
            erros += 1 
    else:
        print("Digite apenas uma letra de cada vez.")

else:
    print("Que pena, todas as suas vidas acabaram :(")