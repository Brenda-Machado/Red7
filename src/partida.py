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
        self.jogadorVez.initialize(1)
        self.jogadorOutro.initialize(2)
        self.baralho = []
        for i in range(7):
            for j in range(7):
                self.baralho.append((j, i))
    
    def getStatus(self):
        return self.status
    
    def getJoagadorVez(self):
        return self.jogadorVez

    def getJoagadorOutro(self):
        return self.jogadorOutro
    
    def atualizaJogador(self, jogada):
        if jogada == 0:
            self.jogadorVez.ja_baixou = True
        elif jogada == 1:
            self.jogadorVez.ja_mudou = True
    
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
            baralho1.append({"cor": carta[0], "numero": carta[1]})
            self.baralho.remove(carta)
            carta = random.choice(self.baralho)
            baralho2.append({"cor": carta[0], "numero": carta[1]})
            self.baralho.remove(carta)

        self.jogadorVez.criaMao(baralho1)
        self.jogadorOutro.criaMao(baralho2)
    
    def atualizaMao(self, carta):
        self.jogadorVez.mao.remove(carta)
    
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