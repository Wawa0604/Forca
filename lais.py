print ("Joguinho da forca - cores")

import random
# tentativa de jogo da forca

# lista de cores para serem sorteadas
open ("cores.txt","r")
# sortear uma palavra
sorteio = random.choice("cores.txt")

sorteioEscondido = sorteio.replace(sorteio, '_' * len(sorteio))

while "_" in sorteioEscondido:

    print (sorteioEscondido)
    chute = input ("Chute uma letra ")

    for i in range(len(sorteio)):
        if sorteio[i] == chute:
            sorteioEscondido = sorteioEscondido [:i] + chute + sorteioEscondido [i+1:]
    
    if chute == sorteio:
        break
print ("Você acertou!!!")