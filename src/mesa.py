"""
Brenda Silva Machado
Descrição: Classe que define a mesa do jogo
"""

from paleta import Paleta
from partida import Partida
from carta import Carta

class Mesa():
    def __init__(self):
        self.mesaJogador1 = {} # recebe uma tupla em que o primeiro é cor e o segundo é número
        self.mesaJogador2 = {}
        self.paleta = None
        self.regraAtual = 0
    
    def getMesaJogador1(self):
        return self.mesaJogador1
    
    def getMesaJogador2(self):
        return self.mesaJogador2
    
    def mudaRegra(self, cor):
        self.regraAtual = cor
        self.paleta.mudaRegra(cor)
    
    def inicioPartida(self):
        self.paleta = Paleta()
    
    def avaliaVitoria(self):
        color = self.paleta.getCorAtual()
        jogadorVez = Partida.getJogadorVez()
        jogadorOutro = Partida.getJogadorOutro()
        resultado_avaliação = False
        if color == 0:
            resultado_avaliação = self.avaliaRegraVermelha(jogadorVez, jogadorOutro)
        elif color == 1:
            resultado_avaliação = self.avaliaRegraLaranja(jogadorVez, jogadorOutro)
        elif color == 2:
            resultado_avaliação = self.avaliaRegraAmarela(jogadorVez, jogadorOutro)
        elif color == 3:
            resultado_avaliação = self.avaliaRegraVerde(jogadorVez, jogadorOutro)
        elif color == 4:
            resultado_avaliação = self.avaliaRegraAzul(jogadorVez, jogadorOutro)
        elif color == 5:
            resultado_avaliação = self.avaliaRegraIndigo(jogadorVez, jogadorOutro)
        else:
            resultado_avaliação = self.avaliaRegraRoxa(jogadorVez, jogadorOutro)
        return resultado_avaliação

    def avaliaRegraVermelha(self, jogadorVez, jogadorOutro):
        maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'vermelho')
        maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'vermelho')
        if maior_j_vez != maior_j_o:
            if maior_j_vez > maior_j_o:
                return True
            else:
                return False
        else:
            cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'vermelho')
            cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'vermelho')
            if cor_m_j_vez < cor_m_j_o:
                return True
            else:
                return False
    
    def avaliaRegraLaranja(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaRepetição(jogadorVez.id)
        num_j_o = self.contaRepetição(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'laranja')
            maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'laranja')
            if maior_j_vez != maior_j_o:
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
            else:
                cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'laranja')
                cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'laranja')
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
    
    def avaliaRegraAmarela(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaCartasMesmaCor(jogadorVez.id)
        num_j_o = self.contaCartasMesmaCor(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'amarelo')
            cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'amarelo')
            if cor_m_j_vez != cor_m_j_o:
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
            else:
                maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'amarelo')
                maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'amarelo')
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
    
    def avaliaRegraVerde(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaCartasPares(jogadorVez.id)
        num_j_o = self.contaCartasPares(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'verde')
            maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'verde')
            if maior_j_vez != maior_j_o:
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
            else:
                cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'verde')
                cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'verde')
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
    
    def avaliaRegraAzul(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaCoresDiferentes(jogadorVez.id)
        num_j_o = self.contaCoresDiferentes(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'azul')
            cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'azul')
            if cor_m_j_vez != cor_m_j_o:
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
            else:
                maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'azul')
                maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'azul')
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
    
    def avaliaRegraIndigo(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaCartasSequencia(jogadorVez.id)
        num_j_o = self.contaCartasSequencia(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'indigo')
            maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'indigo')
            if maior_j_vez != maior_j_o:
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
            else:
                cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'indigo')
                cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'indigo')
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
    
    def avaliaRegraRoxa(self, jogadorVez, jogadorOutro):
        num_j_vez = self.contaCartasMenor4(jogadorVez.id)
        num_j_o = self.contaCartasMenor4(jogadorOutro.id)
        if num_j_vez != num_j_o:
            if num_j_vez > num_j_o:
                return True
            else:
                return False
        else:
            maior_j_vez = self.maiorMesa(jogadorVez.id, flag = 'roxo')
            maior_j_o = self.maiorMesa(jogadorOutro.id, flag = 'roxo')
            if maior_j_vez != maior_j_o:
                if maior_j_vez > maior_j_o:
                    return True
                else:
                    return False
            else:
                cor_m_j_vez = self.menorCor(jogadorVez.id, flag = 'roxo')
                cor_m_j_o = self.menorCor(jogadorOutro.id, flag = 'roxo')
                if cor_m_j_vez < cor_m_j_o:
                    return True
                else:
                    return False
    
    def maiorMesa(self, id, flag):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        
        if flag == 'vermelho':
            maior = 0
            for carta in mesa:
                if carta[1] > maior:
                    maior = carta[1]
            return maior
        elif flag == 'laranja':
            
