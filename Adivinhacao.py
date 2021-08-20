import random
def jogar():

    print("********************************")
    print("Bem vindo no jogo de Advinhação!")
    print("********************************")


    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel: "))
    if( nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    while nivel <= 0 or nivel > 3:
        print("Você deve escolher um número entre 1 e 3 seu burro!")




    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} tentativas".format(rodada,total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)/3
            pontos = round(pontos - pontos_perdidos)

if(__name__=="__main__"):
    jogar()





