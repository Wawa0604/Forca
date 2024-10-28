print ("Joguinho da forca - cores")

import random
# tentativa de jogo da forca

# lista de cores para serem sorteadas
cor = ["azul", "purpura", "turquesa", "cinza", "amarelo", "marinho", "ouro", "prata", "bronze", "coral", "vermelho", "laranja", "marrom", "roxo", "verde", "preto", "rosa", "branco"]
# sortear uma palavra
sorteio = random.choice(cor)

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


# coisas para fazer ainda
#fazer printar as letras que ja foram e checar se uma letra ja foi chutada

# colocar depois que acaba as vidas originais algo como
#  'vc é muito ruim, morreu aqui, bora almentar os acessórios?'