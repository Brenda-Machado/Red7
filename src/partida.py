"""
Brenda Silva Machado
Descrição: Classe que define a partida e a lógica do jogo
"""

from jogador import Jogador
import random

class Partida():
    def __init__(self, jogadorVez: Jogador, jogadorOutro: Jogador):
        self.status = 0
        self.jogadorVez = jogadorVez
        self.jogadorOutro = jogadorOutro
        self.baralho = []
        for i in range(1, 8):
            for j in range(1, 8):
                self.baralho.append((j, i))
    
    def getStatus(self):
        return self.status
    
    def get_jogador(self, id):
        if self.jogadorVez.getId() == id:
            return self.jogadorVez
        elif self.jogadorOutro.getId() == id:
            return self.jogadorOutro

    def getJogadorVez(self):
        return self.jogadorVez

    def getJogadorOutro(self):
        return self.jogadorOutro
    
    def atualizaJogador(self, jogada):
        if jogada == 0:
            self.jogadorVez.setjaBaixou(True)
        elif jogada == 1:
            self.jogadorVez.setjaMudou(True)
    
    def proximaRodada(self):
        self.jogadorVez.atualizaVez()
        self.jogadorOutro.atualizaVez()
        self.jogadorOutro.atualizaVencedor()
    
    def inicioPartida(self):
        self.status = 1
        self.jogadorVez.inicioPartida()
        self.jogadorVez.atualizaVez()
        self.jogadorOutro.inicioPartida()
        baralho1 = []
        baralho2 = []
        for i in range(7):
            carta = random.choice(self.baralho)
            baralho1.append((carta[0], carta[1]))
            self.baralho.remove(carta)
            carta = random.choice(self.baralho)
            baralho2.append((carta[0], carta[1]))
            self.baralho.remove(carta)

        self.jogadorVez.criaMao(baralho1)
        self.jogadorOutro.criaMao(baralho2)
    
    def atualizaMao(self, carta):
        self.jogadorVez.atualizaMao(carta)
    
    def trocaVez(self):
        self.jogadorVez.atualizaVez()
        self.jogadorOutro.atualizaVez()
        self.jogadorVez, self.jogadorOutro = self.jogadorOutro, self.jogadorVez
    
    def fimPartida(self):
        self.status = 3
    
    def abandonoPartida(self):
        self.status = 2
    
    def resetPartida(self):
        self.status = 0



