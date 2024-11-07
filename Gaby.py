import tkinter as tk  #importa tudo da biblioteca
import random

#Configuração da janela INICIAL
janela = tk.Tk()   #incia tkinter: exibe janela
janela.title("Jogo da Forca")   #Define o título da janela 
janela.geometry("1024x520")    #Define o tamanho da janela.
janela.config(bg='#000000')
janela.iconbitmap("favicon.ico") # Define o ícone da janela.


#Widgets dos textos - JANELA INICIAL
textoOrientação1= tk.Label(janela , text="Vamos jogar Forca!" , fg="purple" , bg="black" , font= ("Arial Black" , 20))   #texto que vai aparecer
textoOrientação1.pack()     #aonde ele vai ficar, pack (ordenação padrão)

textoOrientação2= tk.Label(janela , text="Você escolhe o tema e eu te dou uma palavra misteriosa. Chute as letras e complete as lacunas para ganhar." , fg="white" , bg="black" , font= ("Arial" , 12))   #texto que vai aparecer
textoOrientação2.pack()     #aonde ele vai ficar, pack (ordenação padrão)

textoOrientação3= tk.Label(janela , text="Cada letra errada te leva mais perto da forca, mas cada acerto te aproxima da vitória! " , fg="white" , bg="black" , font= ("Arial" , 12))   #texto que vai aparecer
textoOrientação3.pack()     #aonde ele vai ficar, pack (ordenação padrão)

textoOrientação4= tk.Label(janela , text="Clique no tema que você deseja jogar:" , fg="white" , bg="black" , font= ("Arial Bold" , 15))   #texto que vai aparecer
textoOrientação4.place(relx=0.5, rely=0.8, anchor="center")     #aonde ele vai ficar, pack (ordenação padrão)


#Widget da imagem - JANELA INICIAL
imagemInicial = tk.PhotoImage(file="icon.png")   #qual é a imagem
imagem = tk.Label(width=230, height=230, bg="white", image=imagemInicial)  #definindo tamanho e cor
imagem.place(relx=0.5, rely=0.5, anchor="center") #reposicionamento da imagem na tela


#Abrir janelas novas para o jogo (CORES, FRUTAS E OBJETOS)
#Janela de CORES
def abrirJogoCores():
	#Config da janela
	janela2 = tk.Toplevel()
	janela2.title('Jogo da forca')
	janela2.geometry("1024x520")
	janela2.config(bg='#000000')
	janela2.iconbitmap("favicon.ico")

	#Sortear palavra
	cor = ["azul", "purpura", "turquesa", "cinza", "amarelo", "marinho", "ouro", "prata", "bronze", "coral", "vermelho", "laranja", "marrom", "roxo", "verde", "preto", "rosa", "branco"]
	sorteio = random.choice(cor)
	sorteioEscondido = '_' * len(sorteio)

    # Função para processar o chute
	def chutarLetra():
		nonlocal sorteioEscondido
		chute = entrada.get().lower()
		novaLetra = list(sorteioEscondido)
		letrasErradas= []
		#contador=0

        # Atualiza a palavra oculta se o chute estiver correto
		for i in range(len(sorteio)):
			if sorteio[i] == chute:
				novaLetra[i] = chute
				#contador +=1

		sorteioEscondido = ''.join(novaLetra)
		palavra.config(text=sorteioEscondido)
		entrada.delete(0, tk.END)

		if sorteioEscondido==sorteio:
			resultado=tk.Label(janela2, text="Você acertou!", font=("Arial Black", 20), fg="white", bg="black")
			resultado.place(relx=0.5,rely=0.3,anchor="center")
		if chute not in sorteio:
			letrasErradas.append(chute)
			
	#textoContador=tk.Label(janela2, text=textoContador)
	#textoContador.place(relx=0.4,rely=0.6,anchor="center")
	
    #Textos e orientações:
	textoInicial = tk.Label(janela2, text="Consegue adivinhar a cor?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.pack()

	orientação=tk.Label(janela2, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.pack()
	
	palavra=tk.Label(janela2,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 22))
	palavra.place(relx=0.5, rely=0.4, anchor="center")

	#Onde ficam as letras erradas
	letras=tk.Label(janela2, text="Letras erradas:", fg="white", bg="black", font=("Arial", 10))
	letras.place(relx=0.5, rely=0.7, anchor="center")

	
    #Botoes e entrada:
	botao_voltar = tk.Button(janela2, text = 'Voltar para a tela inicial', command = janela2.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela2, text="Chutar", bg="purple", fg="white", font=("Arial", 14), command=chutarLetra)
	botaoChutar.place(relx=0.6,rely=0.6, anchor="center")
	
	entrada=tk.Entry(janela2, width=4, font=("Arial", 20))
	entrada.place(relx=0.5, rely=0.6, anchor="center")
	
	
#Janela de FRUTAS
def abrirJogoFrutas():
	#Config Janela:
	janela3 = tk.Toplevel()
	janela3.title('Jogo da forca')
	janela3.geometry("1024x520")
	janela3.config(bg='#000000')
	janela3.iconbitmap("favicon.ico")

	#Sortear palavra
	cor = ["azul", "purpura", "turquesa", "cinza", "amarelo", "marinho", "ouro", "prata", "bronze", "coral", "vermelho", "laranja", "marrom", "roxo", "verde", "preto", "rosa", "branco"]
	sorteio = random.choice(cor)
	sorteioEscondido = '_ ' * len(sorteio)

	#Area do resultado final
	resultado=tk.Label(janela3, text="Você perdeu/Você ganhou!", font=("Arial Black", 20), fg="white", bg="black")
	resultado.place(relx=0.5,rely=0.3,anchor="center")
	
	#Texto e orientação:
	textoInicial = tk.Label(janela3, text="Consegue adivinhar a fruta?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.pack()
	
	orientação=tk.Label(janela3, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.pack()

	#Onde fica a lacuna/palavra
	palavra=tk.Label(janela3,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 22))
	palavra.place(relx=0.5, rely=0.4, anchor="center")

	#Onde ficam as letras erradas
	letras=tk.Label(janela3, text="Letras erradas:", fg="white", bg="black", font=("Arial", 10))
	letras.place(relx=0.5, rely=0.7, anchor="center")
	
	#Botões e entrada:
	botao_voltar = tk.Button(janela3, text = 'Voltar para a tela inicial', command = janela3.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela3, text="Chutar", bg="purple", fg="white", font=("Arial", 14))
	botaoChutar.place(relx=0.6,rely=0.6, anchor="center")
	  
	entrada=tk.Entry(janela3, width=4, font=("Arial", 20))
	entrada.place(relx=0.5, rely=0.6, anchor="center")	

#Janela de OBJETOS
def abrirJogoObjetos():
	#Config janela:
	janela4 = tk.Toplevel()
	janela4.title('Jogo da forca')
	janela4.geometry("1024x520")
	janela4.config(bg='#000000')
	janela4.iconbitmap("favicon.ico")

	#Sortear palavra
	cor = ["azul", "purpura", "turquesa", "cinza", "amarelo", "marinho", "ouro", "prata", "bronze", "coral", "vermelho", "laranja", "marrom", "roxo", "verde", "preto", "rosa", "branco"]
	sorteio = random.choice(cor)
	sorteioEscondido = '_ ' * len(sorteio)

	#Area do resultado final
	resultado=tk.Label(janela4, text="Você perdeu/Você ganhou!", font=("Arial Black", 20), fg="white", bg="black")
	resultado.place(relx=0.5,rely=0.3,anchor="center")
	
	#Textos e orientações:
	textoInicial = tk.Label(janela4, text="Consegue adivinhar o objeto?" , fg="purple" , bg="black" , font= ("Arial Black" , 20))
	textoInicial.pack()

	orientação=tk.Label(janela4, text="Chute uma letra no input abaixo e aperte no botão chutar para validar" , fg="white", bg="black", font= ("Arial", 14))
	orientação.pack()
	
	palavra=tk.Label(janela4,text=sorteioEscondido, fg="purple", bg="black", font= ("Arial Black", 22))
	palavra.place(relx=0.5, rely=0.4, anchor="center")

	#Onde ficam as letras erradas
	letras=tk.Label(janela4, text="Letras erradas:", fg="white", bg="black", font=("Arial", 10))
	letras.place(relx=0.5, rely=0.7, anchor="center") 
	
	#Botões e entrada:
	botao_voltar = tk.Button(janela4, text = 'Voltar para a tela inicial', command = janela4.destroy, font=("Arial",10))
	botao_voltar.place(relx=0.5, rely=0.9, anchor="center")
	
	botaoChutar=tk.Button(janela4, text="Chutar", bg="purple", fg="white", font=("Arial", 14))
	botaoChutar.place(relx=0.6,rely=0.6, anchor="center")
	
	entrada=tk.Entry(janela4, width=4, font=("Arial", 20))
	entrada.place(relx=0.5, rely=0.6, anchor="center")
	

#Botões para iniciar o jogo - baseado no tema escolhido - PAGINA INICIAL
botIniciar1= tk.Button(janela, text="Cores" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoCores)
botIniciar1.place(relx=0.2, rely=0.9, anchor="center")

botIniciar2= tk.Button(janela, text="Frutas" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoFrutas)
botIniciar2.place(relx=0.5, rely=0.9, anchor="center")

botIniciar3= tk.Button(janela, text="Objetos" , font=("Arial Bold", 14), width=12, height=1, bg="purple", fg="white", command=abrirJogoObjetos)
botIniciar3.place(relx=0.8, rely=0.9, anchor="center")


#Fim
janela.mainloop()  #trava o frame de execucao