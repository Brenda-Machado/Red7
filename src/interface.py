"""
Brenda Silva Machado
Descrição: Classe responsável pela interface do usuário e conexão com o DOG Server
"""

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
import random
from partida import Partida
from mesa import Mesa
from jogador import Jogador


class Interface(DogPlayerInterface):
	def __init__(self):
		self.mainWindow = Tk()
		self.mainWindow.title("Red7")
		self.mainWindow.geometry("1200x900")
		self.mainWindow.resizable(False, False)
		self.mainWindow["bg"]="white"
		self.initFrame = Frame(self.mainWindow)
		self.tableFrame = Frame(self.mainWindow)
		self.tablePlayer1Frame = Frame(self.mainWindow)
		self.tablePlayer2Frame = Frame(self.mainWindow)
		self.butttonFrame = Frame(self.mainWindow)
		self.handFrame = Frame(self.mainWindow)
		self.paletaFrame = Frame(self.mainWindow)
		self.messageFrame = Frame(self.mainWindow)
		self.initView=[]
		self.tableView=[]
		self.buttonView=[]
		self.handView=[]
		self.paletaView=[]
		self.messageView=[]
		self.tablePlayer1View = []
		self.tablePlayer2View = [] 

		self.mesa = None
		self.jogador1 = None
		self.jogador2 = None
		self.partida = None
		self.start_status = None
		self.carta_retirar = None
		self.cor_mudar = None
		self.mesa_jogador1 = []
		self.mesa_jogador2 = []
		self.baralho_jogador1 = []
		self.baralho_jogador2 = []
		self.player_local_id = None
	
		self.loadImages()
		self.loadBaralho()
		self.telaInicial()
		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self.dog_server_interface = DogActor()
		message = self.dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)
		self.mainWindow.mainloop()

	def loadImages(self):
		self.paleta = []
		self.mainWindow.iconphoto(False, PhotoImage(file="images/icon.png"))
		self.table = PhotoImage(file="images/table2.png")
		self.logo = PhotoImage(file="images/logo.png")
		self.paleta.append(PhotoImage(file="images/paleta/vermelho.png"))
		self.paleta.append(PhotoImage(file="images/paleta/laranja.png"))
		self.paleta.append(PhotoImage(file="images/paleta/amarelo.png"))
		self.paleta.append(PhotoImage(file="images/paleta/verde.png"))
		self.paleta.append(PhotoImage(file="images/paleta/azul.png"))
		self.paleta.append(PhotoImage(file="images/paleta/indigo.png"))
		self.paleta.append(PhotoImage(file="images/paleta/roxo.png"))
		self.initView.append(Label(self.initFrame, image=self.logo))

	def loadBaralho(self):
		self.deckCards = [[None for _ in range(7)] for _ in range(7)]
		self.deck = Image.open("images/cards_deck.png")
		for i in range(0, 7):
			for j in range(0, 7):
				self.deckCards[i][j] = (ImageTk.PhotoImage(self.deck.crop((99*(j-1), 148*(i-1), 99*j, 148*i))))


	def createTable(self):
		self.tableView.append(Label(self.tableFrame, image=self.table))
		self.tableView[0].grid(row=0, column=0)

	def definePaleta(self, cor):
		self.paletaView.clear()
		self.paletaView.append(Label(self.paletaFrame, image=self.paleta[cor]))
		self.paletaView[0].grid(row=0, column=0)
		

	def createHand(self, jogador_id):
		baralho = []
		count = 0
		jogador = self.partida.get_jogador(jogador_id)
		baralho = jogador.getMao()
		for carta in baralho:
			cor = carta.getCor()
			numero = carta.getNumero()
			if jogador_id == 1:	
				self.baralho_jogador1.append((cor, numero))
			else:
				self.baralho_jogador2.append((cor, numero))
			print("Cor: ", cor, "Numero: ", numero)		
			self.handView.append(Label(self.handFrame, image=self.deckCards[cor-1][numero-1]))
			self.handView[count].grid(row = 0, column=count)
			count += 1

	def createButtonIniciar(self):
		self.initView.append(Button(self.butttonFrame, text="Iniciar", command=self.iniciarPartida))
		self.initView[1].grid(row=0, column=1)
	
	def createButtons(self):
		self.buttonView.append(Button(self.butttonFrame, text="Passar Turno", command=self.passarTurno))
		self.buttonView.append(Button(self.butttonFrame, text="Baixar Carta", command=self.baixarCarta))
		self.buttonView.append(Button(self.butttonFrame, text="Mudar Paleta", command=self.mudarPaleta))
		self.buttonView[0].grid(row=0, column=1)
		self.buttonView[1].grid(row=0, column=2)
		self.buttonView[2].grid(row=0, column=3)

	def telaInicial(self):
		self.initView[0].grid(row=0, column=0)
		self.createButtonIniciar()
		self.initFrame.pack()
		self.butttonFrame.pack()
	
	def iniciarPartida(self):
		self.start_status = self.dog_server_interface.start_match(2)
		message = self.start_status.get_message()
		messagebox.showinfo(message=message)
		if message == "Partida iniciada":
			players = self.start_status.get_players()
			print(players)
			self.jogador1 = players[0]
			self.jogador2 = players[1]
			self.iniciar()
	
	def iniciar(self):
		self.partida = Partida(Jogador(), Jogador())
		self.mesa = Mesa(self.partida)
		self.partida.jogadorVez.initialize(self.jogador1[2])
		self.partida.jogadorOutro.initialize(self.jogador2[2])
		self.partida.inicioPartida()
		self.initFrame.destroy()
		self.createTable()
		player_local = self.start_status.get_players()
		self.player_local_id = None
		if player_local[0][1] == self.start_status.get_local_id():
			self.player_local_id = player_local[0][2]
		else:
			self.player_local_id = player_local[1][1]
		self.createHand(self.player_local_id)
		self.createButtons()
		self.definePaleta(0)
		self.tableFrame.pack()
		self.handFrame.pack()
		self.paletaFrame.pack()
		self.butttonFrame.pack()
		self.tablePlayer1Frame.pack()
		self.tablePlayer2Frame.pack()
		self.paletaFrame.place(x=1000, y=500)
		self.handFrame.place(x=100, y=700)
		self.butttonFrame.place(x=300, y=600)
		self.tablePlayer1Frame.place(x=100, y=500)
		self.tablePlayer2Frame.place(x=100, y=300)

	def receive_start(self, start_status):
		message = start_status.get_message()
		messagebox.showinfo(message=message)
	
	def passarTurno(self):
		jogador = self.partida.getJogadorVez()
		if self.player_local_id == jogador.getId():
			vitoria_rodada = self.mesa.avaliaVitoria()
			if vitoria_rodada:
				self.partida.proximaRodada()
				self.messageView.clear()
				self.messageView.append(Label(self.tableFrame, text="Passou o turno"))
				self.messageView[0].grid(row=0, column=0)
				self.messageView[0].place(x=500, y=500)
				self.messageFrame.pack()
			else:
				self.partida.fimPartida()
				self.mensagemDerrota()
		
	def baixarCarta(self):
		jogador = self.partida.getJogadorVez()
		if self.player_local_id == jogador.getId():
			if jogador.getJaBaixou() == False:
				self.messageView.clear()
				self.messageView.append(Label(self.tableFrame, text="Selecione uma carta"))
				self.messageView[0].grid(row=0, column=0)
				self.messageView[0].place(x=500, y=500)
				self.messageFrame.pack()
				for i in range(0, 7):
					self.handView[i].bind("<Button-1>", lambda event, i=i: self.selecionarCarta(i, 0))

	def mudarPaleta(self):
		jogador = self.partida.getJogadorVez()
		if self.player_local_id == jogador.getId():
			if jogador.getJaMudou() == False:
				self.messageView.clear()
				self.messageView.append(Label(self.tableFrame, text="Mudou a paleta"))
				self.messageView[0].grid(row=0, column=0)
				self.messageView[0].place(x=500, y=500)
				self.messageFrame.pack()
				for i in range(0, 7):
					self.handView[i].bind("<Button-1>", lambda event, i=i: self.selecionarCarta(i, 1))

	def selecionarCarta(self, i, operacao):
		self.messageView.clear()
		if operacao == 0:
			jogador = self.partida.getJogadorVez()
			if jogador.id == 1:
				self.partida.atualizaMao(self.baralho_jogador1[i])
				self.carta_retirar = i
				self.mesa.atualizaMesa(self.baralho_jogador1[i])
			else:
				self.partida.atualizaMao(self.baralho_jogador2[i])
				self.carta_retirar = i
				self.mesa.atualizaMesa(self.baralho_jogador2[i])
				self.adicionarCarta(self.carta_retirar)
			self.partida.atualizaJogador(0)
		else:
			jogador = self.partida.getJogadorVez()
			if jogador.id == 1:
				if self.baralho_jogador1[i][0] != self.mesa.paleta.getCorAtual():
					self.partida.atualizaMao(self.baralho_jogador1[i])
					self.mesa.mudaRegra(self.baralho_jogador1[i][0])
					print(self.baralho_jogador1[i][0])
					self.cor_mudar = self.baralho_jogador1[i][0]
					self.carta_retirar = i				
			else:
				if self.baralho_jogador2[i][0] != self.mesa.paleta.getCorAtual():
					self.partida.atualizaMao(self.baralho_jogador2[i])
					self.mesa.mudaRegra(self.baralho_jogador2[i][0])
					print(self.baralho_jogador2[i][0])
					self.cor_mudar = self.baralho_jogador2[i][0]
					self.carta_retirar = i
			self.partida.atualizaJogador(1)
		self.receberJogada(operacao)

	def receberJogada(self, jogada):
		if jogada == 1:
			self.definePaleta(self.cor_mudar-2)
		self.handView[self.carta_retirar].place(x=500, y=500)
		self.messageView.clear()

	def adicionarCarta(self, carta):
		cor = self.baralho_jogador2[carta][0]
		numero = self.baralho_jogador2[carta][1]
		if self.start_status.get_local_id() == 1:
			carta_label = Label(self.tablePlayer1Frame, image=self.deckCards[cor-1][numero-1])
			carta_label.grid(row=0, column=len(self.tablePlayer1View))
			self.tablePlayer1View.append(carta_label)
		else:
			carta_label = Label(self.tablePlayer2Frame, image=self.deckCards[cor-1][numero-1])
			carta_label.grid(row=0, column=len(self.tablePlayer2View))
			self.tablePlayer2View.append(carta_label)
	
	def receive_withdrawal_notification(self):
		self.partida.abandonoPartida()
		self.messageView.clear()
		self.messageView.append(Label(self.tableFrame, text="Oponente desconectou"))
		self.messageView[0].grid(row=0, column=0)
		self.messageView[0].place(x=500, y=500)
		self.messageFrame.pack()

Interface()

