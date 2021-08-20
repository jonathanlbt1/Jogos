import forca, Adivinhacao


print("********************************")
print("******Escollha o seu jogo!******")
print("********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    Adivinhacao.jogar()

# if(__name__=="__main__"):
#     jogar()

