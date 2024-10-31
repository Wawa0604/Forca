#%%
#SÓ TESTE!!!!!!
#Primeiro passo: importar bibliotecas
import random

#Segundo passo: mensagem de boas vindas
print ("Descubra a cor!")

#Terceiro passo: ler o arquivo
meuArquivo = open ('cores.txt')

with open('cores.txt', 'r') as reader:
    lista = reader.readlines()
    #print(lista)
    #print(lista[3])
#Quarto passo: fazer ele escolher
    # corEscolhida= random.choice(lista)
    # print(lista)
# Sortear um nome aleatório
def sorteaiaCor(cor):
    return random.choice(cor)

# Carregar os nomes do arquivo

# Sortear um nome aleatório
cor_sorteada = random.choice(lista)

# Exibir o nome sorteado
print(f'O nome sorteado foi: {cor_sorteada}')

# %%
