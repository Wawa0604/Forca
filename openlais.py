#%%
#Primeiro passo: importar bibliotecas
import random

#Segundo passo: mensagem de boas vindas
print ("Descubra a cor!")

#Terceiro passo: ler o arquivo
meuArquivo = open ('cores.txt')

with open('cores.txt', 'r') as reader:
    lista = reader.readlines()
    
#Quarto passo: fazer ele escolher
def sorteaiaCor(cor):
    return random.choice(cor)

# Sortear um nome aleatório
cor_sorteada= random.choice(lista)

# Exibir o nome sorteado
print(f'O nome sorteado foi: {cor_sorteada}')

#Parte Isa:
sorteioEscondido = cor_sorteada.replace(cor_sorteada, '_' * len(cor_sorteada))
#contador de chances
contador = 0
#lista de letras ja chutadas
letrasJaChutadas = []
#lista das letras certas já chutadas para avisar se já chutou antes 
#letrasCertas = []
#verificar se os chutes são letras e apenas uma
while True:

    #enquanto a palavra estiver com letras escondidas
    while "_" in sorteioEscondido:

        # mostrar as letras escondidas
        print (sorteioEscondido)
        # print ("Seus chutes anteriores:", letrasErradas) #printar as q ja foram
        # print(contador)#linha para organização
        #imput para os chutes
        chute = input ("Chute uma letra ")
        
        #verificar se os chutes são letras e apenas uma
        if len(chute) == 1 and chute.isalpha():

            #armazenas as letras já chutadas para perder chances
            # printar as q ja foram    
            for i in range(len(cor_sorteada)):
                if cor_sorteada[i] == chute:
                    sorteioEscondido = sorteioEscondido [:i] + chute + sorteioEscondido [i+1:]

                #mensagem de aviso caso uma letra ja tenha ido
                #não computar ela na contagem de vidas
                #mensagem para quando der mais chutes q permitido
                    if chute == cor_sorteada:
                        break

        else:
            print("Por favor insira UMA LETRA")
    break
 
print ("Você acertou!!!")
   

# %%
