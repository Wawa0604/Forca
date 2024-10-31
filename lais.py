'''
print ("Joguinho da forca - cores")

import random
# tentativa de jogo da forca

# lista de cores para serem sorteadas
cor= open ("cores.txt",'r')
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
'''
#%%

import random

#tema= (input ("Bem-vindo ao jogo da forca! Escolha com qual tema você quer jogar: frutas, cores ou objetos: "))
#cor= open("cores.txt", 'r')


#if tema == 'cores':
    # with open ("cores.txt", 'r') as reader:
    #     corSorteada= random.choice()
    #     print (corSorteada)

teste= open ("cores.txt",'r')
print (teste)



# %%
# Procura uma palavra-chave em cada linha
with open('cores.txt', 'r') as reader:
    while True:
        linha = reader.readline()
        if not linha:  # Fim do arquivo
            break
        if "teste" in linha:
            print(f"Palavra encontrada: {linha}")
            break
        else:
            print(f"Palavra não encontrada")
# %%
#Sorteio de nomes
import random

# Caminho do arquivo de nomes
arquivoTXT = r'C:\Users\thiag\OneDrive\Documentos\GitHub\cursoPython\Testes\nomes.txt'

# Carregar a lista de nomes do arquivo
def carregarNomes(arquivo):
    with open(arquivo, 'r') as f:
        nomes = f.read().splitlines()
    return nomes

# Sortear um nome aleatório
def sorteaiaNome(nomes):
    return random.choice(nomes)

# Carregar os nomes do arquivo
nomes = carregarNomes(arquivoTXT)

# Sortear um nome aleatório
nome_sorteado = sorteaiaNome(nomes)

# Exibir o nome sorteado
print(f'O nome sorteado foi: {nome_sorteado}')

# # Contar o número de nomes
# numero_de_nomes = len(nomes)

# # Exibir o número de nomes
# print(f'O número de nomes no arquivo é: {numero_de_nomes}')

# # Imprimir a posição (índice) e o nome de cada item na lista
# for indice, nome in enumerate(nomes):
#     print(f'Índice: {indice}, Nome: {nome}')