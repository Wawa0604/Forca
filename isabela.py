print ("Joguinho da forca - cores")

import random

# lista de cores para serem sorteadas
cor = ["azul", "purpura", "turquesa", "cinza", "amarelo", "marinho", "ouro", "prata", "bronze", "coral", "vermelho", "laranja", "marrom", "roxo", "verde", "preto", "rosa", "branco"]
# sortear uma palavra
sorteio = random.choice(cor)
#esconder a palavra sorteada


sorteioEscondido = sorteio.replace(sorteio, '_' * len(sorteio))
#contador de chances
contador = 0
#lista de letras ja chutadas
letrasErradas = []
#lista das letras certas já chutadas para avisar se já chutou antes 
letrasCertas = []
#verificar se os chutes são letras e apenas uma

    #enquanto a palavra estiver com letras escondidas
while "_" in sorteioEscondido and contador < 6:

        # mostrar as letras escondidas
    print (sorteioEscondido)
    print ("Seus chutes anteriores:", letrasErradas) #printar as q ja foram
    print(contador)#linha para organização
        #imput para os chutes
    chute = input ("Chute uma letra ")
        
    if len(chute) == 1 and chute.isalpha():
        
        if chute not in letrasCertas and chute not in letrasErradas:
                
            for i in (sorteio):
                #contador2 = 0
                if i == chute:
                    sorteioEscondido = sorteioEscondido [:i] + chute + sorteioEscondido [i+1:]
                    letrasCertas.append(chute)

        else:
                        #armazenar as letras já chutadas para perder chances
            contador += 1
            letrasErradas.append(chute)
    else:
        print("Você já chutou essa letra.")
 
if contador >= 6:
    print ("infelismente Alex foi enforcado")

else:
    print ("Você acertou!!!")
   
   
# coisas para fazer ainda:

#fazer printar as letras que ja foram e checar se uma letra ja foi chutada

# colocar depois que acaba as vidas originais algo como
#  'vc é muito ruim, morreu aqui, bora almentar os acessórios?'

#para enviar o jogo, subir no git um sorce code, um relese para quem não quiser baixar e um read me esplicando o jogo 
       #verificar se os chutes são letras e apenas uma

'''
        if len(chute) == 1 and chute.isalpha():

            #armazenar as letras já chutadas para perder chances
            #printar as q ja foram
            for i in range(len(sorteio)):
                if sorteio[i] == chute:
                    sorteioEscondido = sorteioEscondido [:i] + chute + sorteioEscondido [i+1:]
                    letrasCertasJaChutadas.append(chute)

                elif sorteio[i] != chute:
                    contador += 1
                    letrasErradasJaChutadas.append(chute)

                elif chute in letrasCertasJaChutadas or letrasErradasJaChutadas:
                    print("Você já chutou essa letra")
      
                #mensagem de aviso caso uma letra ja tenha ido 
                #não computar ela na contagem de vidas
                #Mensagem para quando der mais chutes q permitido
                    if chute == sorteio:
                      break
            else:
                    print ("Por favor insira UMA LETRA")
     '''