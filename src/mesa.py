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
        self.paleta = Paleta()
        self.regraAtual = 0
        self.cartaConsiderada1 = None
        self.cartaConsiderada2 = None # cartas que servem para a avaliação da regra dentro das flags
    
    def getMesaJogador1(self):
        return self.mesaJogador1
    
    def getMesaJogador2(self):
        return self.mesaJogador2
    
    def mudaRegra(self, cor):
        self.regraAtual = cor
        self.paleta.mudaRegra(cor)

    def atualizaMesa(self, carta):
        jogadorVez = Partida.getJogadorVez()
        if jogadorVez.id == 1:
            self.mesaJogador1[carta.cor] = carta.numero
        else:
            self.mesaJogador2[carta.cor] = carta.numero
    
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
        num_j_vez = self.contaRepeticao(jogadorVez.id)
        num_j_o = self.contaRepeticao(jogadorOutro.id)
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
            cartaConsiderada = self.cartaConsiderada1
        else:
            mesa = self.mesaJogador2
            cartaConsiderada = self.cartaConsiderada2
        
        if flag == 'vermelho' or flag == 'azul':
            maior = 0
            for carta in mesa:
                if carta[1] > maior:
                    maior = carta[1]
            return maior
        elif flag == 'laranja' or flag == 'indigo':
            return cartaConsiderada[1]
        elif flag == 'amarelo':
            cor = cartaConsiderada[0]
            maior = 0
            for carta in mesa:        
                if carta[0] == cor and carta[1] > maior:
                    maior = carta[1]
            return maior
        elif flag == 'verde':
            maior = 0
            for carta in mesa:
                if carta[1] > maior and carta[1] % 2 == 0:
                    maior = carta[1]
            return maior
        elif flag == 'roxa':
            maior = 0
            for carta in mesa:
                if carta[1] > maior and carta[1] < 4:
                    maior = carta[1]
            return maior
    
    def menorCor(self, id, flag):
        if id == 1:
            mesa = self.mesaJogador1
            cartaConsiderada = self.cartaConsiderada1
        else:
            mesa = self.mesaJogador2
            cartaConsiderada = self.cartaConsiderada2
        
        if flag == 'vermelho' or flag == 'azul':
            menor = 7
            for carta in mesa:
                if carta[0] < menor:
                    menor = carta[0]
            return menor
        elif flag == 'laranja':
            numero = cartaConsiderada[1]
            menor = 7
            for carta in mesa:
                if carta[1] == numero and carta[0] < menor:
                    menor = carta[0]
            return menor
        elif flag == 'amarela' or flag == 'indigo':
            return cartaConsiderada[0]
        elif flag == 'verde':
            menor = 7
            for carta in mesa:
                if carta[0] < menor and carta[1] % 2 == 0:
                    menor = carta[0]
            return menor
        elif flag == 'roxo':
            menor = 7
            for carta in mesa:
                if carta[0] < menor and carta[1] < 4:
                    menor = carta[0]
            return menor
    
    def contaRepeticao(self, id):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        repeticoes = 0
        for i in range(1, 7):
            apareceu = 0
            for carta in mesa:
                if carta[1] == 1:
                    apareceu += 1
            if apareceu > repeticoes:
                repeticoes = apareceu
                cartaConsiderada = (i, i)
        if id == 1:
            self.cartaConsiderada1 = cartaConsiderada
        else:
            self.cartaConsiderada2 = cartaConsiderada
        return repeticoes
    
    def contaCartasMesmaCor(self, id):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        mesma_cor = 0
        for i in range(1, 7):
            apareceu = 0
            for carta in mesa:
                if carta[0] == i:
                    apareceu += 1
            if apareceu > mesma_cor:
                mesma_cor = apareceu
                cartaConsiderada = (i, i)
        if id == 1:
            self.cartaConsiderada1 = cartaConsiderada
        else:
            self.cartaConsiderada2 = cartaConsiderada
        return mesma_cor
    
    def contaCartasPares(self, id):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        pares = 0
        for carta in mesa:
            if carta[1] % 2 == 0:
                pares += 1
        return pares
    
    def contaCoresDiferentes(self, id):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        cores = []
        for carta in mesa:
            if carta[0] not in cores:
                cores.append(carta[0])
        return len(cores)
    
    def contaCartasSequencia(self, id):
        if id == 1:
            mesa = list(self.mesaJogador1.values())

        else:
            mesa = list(self.mesaJogador2.values())
        mesa.sort(key=lambda carta: carta[1])  # Ordena as cartas pelo número
        
        maior_sequencia = 1
        sequencia_atual = 1
        maior_carta_sequencia = mesa[0][1]  # Inicializa a maior carta com a primeira carta da mesa
        
        for i in range(1, len(mesa)):
            if mesa[i][1] == mesa[i-1][1] + 1:
                sequencia_atual += 1
                if sequencia_atual > maior_sequencia:
                    maior_sequencia = sequencia_atual
                    maior_carta_sequencia = mesa[i][1]  # Atualiza a maior carta da sequência
            else:
                sequencia_atual = 1
        
        cartaConsiderada = maior_carta_sequencia  # Salva a maior carta da maior sequência
        if id == 1:
            self.cartaConsiderada1 = cartaConsiderada
        else:
            self.cartaConsiderada2 = cartaConsiderada
        return maior_sequencia

    
    def contaCartasMenor4(self, id):
        if id == 1:
            mesa = self.mesaJogador1
        else:
            mesa = self.mesaJogador2
        menor4 = 0
        for carta in mesa:
            if carta[1] < 4:
                menor4 += 1
        return menor4
