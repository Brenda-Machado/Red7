from tkinter import *
from PIL import Image, ImageTk
import random

class Interface:
	def __init__(self):
		self.mainWindow = Tk()
		self.mainWindow.title("Red7")
		self.mainWindow.geometry("1200x900")
		self.mainWindow.resizable(False, False)
		self.mainWindow["bg"]="white"
		self.initFrame = Frame(self.mainWindow)
		self.tableFrame = Frame(self.mainWindow)
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
	
		self.loadImages()
		self.loadBaralho()
		self.telaInicial()
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
		self.deckCards=[]
		self.deck = Image.open("images/cards_deck.png")
		for i in range(1, 8):
			for j in range(1,8):
				self.deckCards.append(ImageTk.PhotoImage(self.deck.crop((99*(j-1), 148*(i-1), 99*j, 148*i))))


	def createTable(self):
		self.tableView.append(Label(self.tableFrame, image=self.table))
		self.tableView[0].grid(row=0, column=0)

	def definePaleta(self, cor):
		self.paletaView.clear()
		self.paletaView.append(Label(self.paletaFrame, image=self.paleta[cor]))
		self.paletaView[0].grid(row=0, column=0)
		

	def createHand(self):
		for i in range(0, 7):
			self.handView.append(Label(self.handFrame, image=random.choice(self.deckCards)))
			self.handView[i].grid(row=0, column=i)
	
	def createButtonIniciar(self):
		self.initView.append(Button(self.butttonFrame, text="Iniciar", command=self.iniciar))
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
	
	def iniciar(self):
		self.initFrame.destroy()
		self.createTable()
		self.createHand()
		self.createButtons()
		self.definePaleta(0)
		self.tableFrame.pack()
		self.handFrame.pack()
		self.paletaFrame.pack()
		self.butttonFrame.pack()
		self.paletaFrame.place(x=1000, y=500)
		self.handFrame.place(x=100, y=700)
		self.butttonFrame.place(x=300, y=650)
	
	def passarTurno(self):
		self.messageView.clear()
		self.messageView.append(Label(self.tableFrame, text="Passou o turno"))
		self.messageView[0].grid(row=0, column=0)
		self.messageView[0].place(x=500, y=500)
		self.messageFrame.pack()
		
	def baixarCarta(self):
		self.messageView.clear()
		self.messageView.append(Label(self.tableFrame, text="Baixou a carta"))
		self.messageView[0].grid(row=0, column=0)
		self.messageView[0].place(x=500, y=500)
		self.messageFrame.pack()

	def mudarPaleta(self):
		self.messageView.clear()
		self.messageView.append(Label(self.tableFrame, text="Mudou a paleta"))
		self.messageView[0].grid(row=0, column=0)
		self.messageView[0].place(x=500, y=500)
		self.messageFrame.pack()
		self.definePaleta(random.randint(0,6))
		
Interface()
