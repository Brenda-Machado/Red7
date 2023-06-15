"""
Brenda Silva Machado
Descrição: Classe que define a partida e a lógica do jogo
"""

from jogador import Jogador

class Partida():
    def __init__(self, jogadorVez: Jogador, jogadorOutro: Jogador):
        self.status = 0
        self.jogadorVez = jogadorVez
        self.jogadorOutro = jogadorOutro
    
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
        self.jogadorVez.criaMao()
        self.jogadorOutro.criaMao()
    
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