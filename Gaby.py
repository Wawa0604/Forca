import tkinter as tk  #importa tudo da biblioteca
import random

# Criação de listas importando dados dos arquivos de texto
with open ('cores.txt', 'r') as reader:

	cor = reader.readlines()

with open ('frutas.txt', 'r') as reader:

	frutas = reader.readlines()

with open ('objetos.txt', 'r') as reader:

	objetos = reader.readlines()

#Configuração da janela INICIAL
janela = tk.Tk()   #incia tkinter: exibe janela
janela.title("Jogo da Forca")   #Define o título da janela 
janela.geometry("1024x520")    #Define o tamanho da janela.
janela.config(bg='#000000')   #Define cor background da janela
janela.iconbitmap("favicon.ico") # Define o ícone da janela.


#Widgets dos textos - JANELA INICIAL
textoOrientação1= tk.Label(janela , text="Vamos jogar Forca!" , fg="purple" , bg="black" , font= ("Arial Black" , 20))   #texto que vai aparecer
textoOrientação1.place(relx=0.5,rely=0.08, anchor="center")     #aonde ele vai ficar

textoOrientação2= tk.Label(janela , text="Você escolhe o tema e eu te dou uma palavra misteriosa. Chute as letras e complete as lacunas para ganhar." , fg="white" , bg="black" , font= ("Arial" , 12))   #texto que vai aparecer
textoOrientação2.place(relx=0.5,rely=0.15, anchor="center")      #aonde ele vai ficar

textoOrientação3= tk.Label(janela , text="Cada letra errada te leva mais perto da forca, mas cada acerto te aproxima da vitória! " , fg="white" , bg="black" , font= ("Arial" , 12))   #texto que vai aparecer
textoOrientação3.place(relx=0.5,rely=0.2, anchor="center")     #aonde ele vai ficar

textoOrientação4= tk.Label(janela , text="Clique no tema que você deseja jogar:" , fg="white" , bg="black" , font= ("Arial Bold" , 15))   #texto que vai aparecer
textoOrientação4.place(relx=0.5, rely=0.8, anchor="center")     #aonde ele vai ficar


#Widget da imagem - JANELA INICIAL
imagemInicial = tk.PhotoImage(file="icon.png")   #qual é a imagem
imagem = tk.Label(width=230, height=230, bg="white", image=imagemInicial)  #definindo tamanho e cor
imagem.place(relx=0.5, rely=0.5, anchor="center") #reposicionamento da imagem na tela


#Abrir janelas novas para o jogo (CORES, FRUTAS E OBJETOS)
#Janela de CORES
def abrirJogoCores():
	#Config da janela
	janela2 = tk.Toplevel()   #criando nova janela!
	janela2.title('Jogo da forca')
	janela2.geometry("1024x520")
	janela2.config(bg='#000000')
	janela2.iconbitmap("favicon.ico")

	#Sortear palavra
	sorteio = random.choice(cor).strip()
	sorteioEscondido = '_' * len(sorteio)
	contador=6
	letras = []

    # Função para processar o chute
	def chutarLetra():
		nonlocal sorteioEscondido, contador  #nonlocal serve pra pegar variavel que ta fora da função
		chute = entrada.get().lower()
		novaLetra = list(sorteioEscondido)

        # Atualiza a palavra oculta se o chute estiver correto
		for i in range(len(sorteio)):
			if sorteio[i] == chute:
				novaLetra[i] = chute

		#Atualiza as lacunas
		sorteioEscondido = ''.join(novaLetra)
		palavra.config(text=sorteioEscondido)
		entrada.delete(0, tk.END)

		#Se acertar:
		if sorteioEscondido==sorteio:
			tentativa.config(text="Você acertou e salvou o Zezinho!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)

		#Se letra não corresponder:
		if chute not in sorteio:
			contador -=1
			tentativa.config(text=f"Você tem {contador} chances de errar a letra")
			letras.append (chute)
			letras_label.config(text=f"Letras erradas: {' '.join(letras)}")
		
		#Se acabar as tentativas:
		if contador <= 0:
			tentativa.config(text="Você perdeu e matou o zezinho!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)
			palavra.config(text=f"Era: {sorteio}", fg="purple", bg="black", font= ("Arial Bold", 22))
	

		#Mudar imagens
		if contador == 5:
			imagemForca.config= tk.PhotoImage(file="imagens/2.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 4:
			imagemForca.config= tk.PhotoImage(file="imagens/3.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 3:
			imagemForca.config= tk.PhotoImage(file="imagens/4.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela			
		if contador == 2:
			imagemForca.config= tk.PhotoImage(file="imagens/5.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 1:
			imagemForca.config= tk.PhotoImage(file="imagens/6.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 0:
			imagemForca.config= tk.PhotoImage(file="imagens/7.png")   #qual é a imagem
			imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela

    #Textos e orientações:
	textoInicial = tk.Label(janela2, text="Consegue adivinhar a cor?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.place(relx=0.5,rely=0.08, anchor="center")

	orientação=tk.Label(janela2, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.place(relx=0.5,rely=0.15, anchor="center")
	
	#Lacunas para a palavra:
	palavra=tk.Label(janela2,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 30))
	palavra.place(relx=0.6, rely=0.45, anchor="center")

	#Onde ficam as letras erradas:
	letras_label = tk.Label(janela2, text=f"Letras erradas: ", fg="white", bg="black", font=("Arial", 14))
	letras_label.place(relx=0.5, rely=0.75, anchor="center")

	#Onde conta as tentativas:
	tentativa=tk.Label(janela2, text="Você tem 6 chances de errar a letra", font=("Arial Bold", 16), fg="white", bg="black")
	tentativa.place(relx=0.5,rely=0.28,anchor="center")
	
    #Botoes e entrada:
	botao_voltar = tk.Button(janela2, text = 'Voltar para a tela inicial', command = janela2.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela2, text="Chutar", bg="purple", fg="white", font=("Arial", 16), command=chutarLetra)
	botaoChutar.place(relx=0.65,rely=0.6, anchor="center")
	
	entrada=tk.Entry(janela2, width=4, font=("Arial", 25))
	entrada.place(relx=0.55, rely=0.6, anchor="center")

	#Imagem Forca
	imagemForca = tk.PhotoImage(file="imagens/1.png")   #qual é a imagem
	imagem = tk.Label(janela2, width=200, height=200, bg="white", image=imagemForca)  #definindo tamanho e cor
	imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
	
	
#Janela de FRUTAS
def abrirJogoFrutas():
	#Config da janela
	janela3 = tk.Toplevel()   #criando nova janela!
	janela3.title('Jogo da forca')
	janela3.geometry("1024x520")
	janela3.config(bg='#000000')
	janela3.iconbitmap("favicon.ico")

	#Sortear palavra
	sorteio = random.choice(frutas).strip()
	sorteioEscondido = '_' * len(sorteio)
	contador=6
	letras = []

    # Função para processar o chute
	def chutarLetra():
		nonlocal sorteioEscondido, contador  #nonlocal serve pra pegar variavel que ta fora da função
		chute = entrada.get().lower()
		novaLetra = list(sorteioEscondido)

        # Atualiza a palavra oculta se o chute estiver correto
		for i in range(len(sorteio)):
			if sorteio[i] == chute:
				novaLetra[i] = chute

		#Atualiza as lacunas
		sorteioEscondido = ''.join(novaLetra)
		palavra.config(text=sorteioEscondido)
		entrada.delete(0, tk.END)

		#Se acertar:
		if sorteioEscondido==sorteio:
			tentativa.config(text="Você acertou e salvou o Alex!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)

		#Se letra não corresponder:
		if chute not in sorteio:
			contador -=1
			tentativa.config(text=f"Você tem {contador} chances de errar a letra")
			letras.append(chute)
			letras_label.config(text=f"Letras Erradas: {' '.join(letras)}")
		
		#Se acabar as tentativas:
		if contador <= 0:
			tentativa.config(text="Você perdeu e matou o Alex!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)
			palavra.config(text=f"Era: {sorteio}", fg="purple", bg="black", font= ("Arial Bold", 22))

		#Mudar imagens
		if contador == 5:
			imagemForca.config= tk.PhotoImage(file="imagens/2.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 4:
			imagemForca.config= tk.PhotoImage(file="imagens/3.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 3:
			imagemForca.config= tk.PhotoImage(file="imagens/4.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela			
		if contador == 2:
			imagemForca.config= tk.PhotoImage(file="imagens/5.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 1:
			imagemForca.config= tk.PhotoImage(file="imagens/6.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 0:
			imagemForca.config= tk.PhotoImage(file="imagens/7.png")   #qual é a imagem
			imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela

    #Textos e orientações:
	textoInicial = tk.Label(janela3, text="Consegue adivinhar a fruta?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.place(relx=0.5,rely=0.08, anchor="center")

	orientação=tk.Label(janela3, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.place(relx=0.5,rely=0.15, anchor="center")
	
	#Lacunas para a palavra:
	palavra=tk.Label(janela3,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 30))
	palavra.place(relx=0.6, rely=0.45, anchor="center")

	#Onde ficam as letras erradas:
	letras_label = tk.Label(janela3, text=f"Letras erradas: ", fg="white", bg="black", font=("Arial", 14))
	letras_label.place(relx=0.5, rely=0.75, anchor="center")

	#Onde conta as tentativas:
	tentativa=tk.Label(janela3, text="Você tem 6 chances de errar a letra", font=("Arial Bold", 16), fg="white", bg="black")
	tentativa.place(relx=0.5,rely=0.28,anchor="center")
	
    #Botoes e entrada:
	botao_voltar = tk.Button(janela3, text = 'Voltar para a tela inicial', command = janela3.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela3, text="Chutar", bg="purple", fg="white", font=("Arial", 16), command=chutarLetra)
	botaoChutar.place(relx=0.65,rely=0.6, anchor="center")
	
	entrada=tk.Entry(janela3, width=4, font=("Arial", 25))
	entrada.place(relx=0.55, rely=0.6, anchor="center")

	#Imagem Forca
	imagemForca = tk.PhotoImage(file="imagens/1.png")   #qual é a imagem
	imagem = tk.Label(janela3, width=200, height=200, bg="white", image=imagemForca)  #definindo tamanho e cor
	imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela

#Janela de OBJETOS
def abrirJogoObjetos():
	#Config da janela
	janela4 = tk.Toplevel()   #criando nova janela!
	janela4.title('Jogo da forca')
	janela4.geometry("1024x520")
	janela4.config(bg='#000000')
	janela4.iconbitmap("favicon.ico")

	#Sortear palavra
	sorteio = random.choice(objetos).strip()
	sorteioEscondido = '_' * len(sorteio)
	contador=6
	letras = []

    # Função para processar o chute
	def chutarLetra():
		nonlocal sorteioEscondido, contador  #nonlocal serve pra pegar variavel que ta fora da função
		chute = entrada.get().lower()
		novaLetra = list(sorteioEscondido)

        # Atualiza a palavra oculta se o chute estiver correto
		for i in range(len(sorteio)):
			if sorteio[i] == chute:
				novaLetra[i] = chute

		#Atualiza as lacunas
		sorteioEscondido = ''.join(novaLetra)
		palavra.config(text=sorteioEscondido)
		entrada.delete(0, tk.END)

		#Se acertar:
		if sorteioEscondido==sorteio:
			tentativa.config(text="Você acertou e salvou o Alex!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)

		#Se letra não corresponder:
		if chute not in sorteio:
			contador -=1
			tentativa.config(text=f"Você tem {contador} chances de errar a letra")
			letras.append (chute)
			letras_label.config(text= f"Letras Erradas: {' '.join(letras)}")
		
		#Se acabar as tentativas:
		if contador <= 0:
			tentativa.config(text="Você perdeu e matou o Alex!", font=("Arial Black", 24), fg="white", bg="black")
			entrada.config(state=tk.DISABLED)
			palavra.config(text=f"Era: {sorteio}", fg="purple", bg="black", font= ("Arial Bold", 22))

		#Mudar imagens
		if contador == 5:
			imagemForca.config= tk.PhotoImage(file="imagens/2.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 4:
			imagemForca.config= tk.PhotoImage(file="imagens/3.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 3:
			imagemForca.config= tk.PhotoImage(file="imagens/4.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela			
		if contador == 2:
			imagemForca.config= tk.PhotoImage(file="imagens/5.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 1:
			imagemForca.config= tk.PhotoImage(file="imagens/6.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela
		if contador == 0:
			imagemForca.config= tk.PhotoImage(file="imagens/7.png")   #qual é a imagem
			imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca.config)  #definindo tamanho e cor
			imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela

    #Textos e orientações:
	textoInicial = tk.Label(janela4, text="Consegue adivinhar o objeto?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.place(relx=0.5,rely=0.08, anchor="center")

	orientação=tk.Label(janela4, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.place(relx=0.5,rely=0.15, anchor="center")
	
	#Lacunas para a palavra:
	palavra=tk.Label(janela4,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 30))
	palavra.place(relx=0.6, rely=0.45, anchor="center")

	#Onde ficam as letras erradas:
	letras_label = tk.Label(janela4, text=f"Letras erradas: ", fg="white", bg="black", font=("Arial", 14))
	letras_label.place(relx=0.5, rely=0.75, anchor="center")
	#Onde conta as tentativas:
	tentativa=tk.Label(janela4, text="Você tem 6 chances de errar a letra", font=("Arial Bold", 16), fg="white", bg="black")
	tentativa.place(relx=0.5,rely=0.28,anchor="center")
	
    #Botoes e entrada:
	botao_voltar = tk.Button(janela4, text = 'Voltar para a tela inicial', command = janela4.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela4, text="Chutar", bg="purple", fg="white", font=("Arial", 16), command=chutarLetra)
	botaoChutar.place(relx=0.65,rely=0.6, anchor="center")
	
	entrada=tk.Entry(janela4, width=4, font=("Arial", 25))
	entrada.place(relx=0.55, rely=0.6, anchor="center")

	#Imagem Forca
	imagemForca = tk.PhotoImage(file="imagens/1.png")   #qual é a imagem
	imagem = tk.Label(janela4, width=200, height=200, bg="white", image=imagemForca)  #definindo tamanho e cor
	imagem.place(relx=0.4, rely=0.52, anchor="center") #reposicionamento da imagem na tela

#Botões para iniciar o jogo - baseado no tema escolhido - PAGINA INICIAL
botIniciar1= tk.Button(janela, text="Cores" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoCores)
botIniciar1.place(relx=0.2, rely=0.9, anchor="center")

botIniciar2= tk.Button(janela, text="Frutas" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoFrutas)
botIniciar2.place(relx=0.5, rely=0.9, anchor="center")

botIniciar3= tk.Button(janela, text="Objetos" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoObjetos)
botIniciar3.place(relx=0.8, rely=0.9, anchor="center")

#Fim
janela.mainloop()  #trava o frame de execucao
