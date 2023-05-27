# Red7 
## 1. Objetivo 
Desenvolvimento de um jogo distribuído para a disciplina Engenharia de Software I (INE5417) que suporte a disputa de partidas de Red7 na modalidade usuário contra usuário, estando os usuários em máquinas diferentes. 

## 2. Definições, abreviaturas 
+ Paleta: termo que se refere à cor que rege aquela rodada;
+ Rodada: designa a vez de um determinado jogador, na qual ele pode fazer um conjunto de ações que pode levar a sua vitória na rodada;
+ Regra: designa uma sentença que cada cor possui, a qual só tem efeito quando essa cor é colocada na paleta e rege o jogo até que a mesma perca o efeito;
+ Tela: diz respeito à região da mesa em que o jogador põe suas cartas;
+ Partida: outro termo para jogatina, ou seja, o conjunto de rodadas do jogo.

## 3. Explicação do jogo
O programa simula uma jogatina de Red7, um jogo de cartas da Asmadi Games e distribuído no Brasil pela PaperGames. O original permite de 2 a 4 jogadores, porém para reduzir a complexidade de desenvolvimento, esse projeto foi adaptado para apenas 2 jogadores. 
O jogo possui um baralho com 49 cartas, sendo que cada carta possui um número de 1 a 7 e uma de sete cores (vermelho, laranja, amarelo, verde, azul, índigo e roxo). Existe apenas uma carta para cada combinação. A ordem de grandeza das cartas, qual carta é mais forte que outra, vai crescendo dos números 1 ao 7 e do roxo para o vermelho. A maior carta do jogo é o 7 vermelho e a menor o 1 roxo. Cada cor possui uma regra associada a ela, descritas na tabela a seguir: 
  
![image](https://user-images.githubusercontent.com/87547436/228386347-63e8e61e-5c81-46ac-9f64-f733da2ded8f.png)

As regras das cartas só fazem efeito quando aquela cor é a cor da paleta, ou seja, enquanto estiver na mão do jogador, a regra não vale para o jogo. À exceção da vermelha, as demais regras dizem respeito à quantidade de cartas, ou seja, o jogador com maior número de cartas na tela que atendam aquele requisito é o vencedor da rodada. 

O objetivo do jogo é sempre ganhar a rodada que joga, ou seja, sempre que for a vez daquele jogador, ele deve garantir que a rodada fique à favor dele, seja mudando a cor da paleta e/ou baixando cartas na sua tela. Caso não seja possível, não haja ações que possam levar à vitória daquele jogador em sua rodada, ele perde a partida.

Caso as cartas de um jogador acabem, ele automaticamente vence o jogo.

Ao iniciar a partida, cada jogador recebe 7 cartas do baralho. A cor da paleta é automaticamente vermelha, antes das rodadas começarem. Um jogador é sorteado para iniciar sua rodada. As ações possíveis para cada jogador em sua rodada são:

+ Baixar uma carta de sua mão na tela;
+ Mudar a cor da paleta.

Ambas as ações só podem ser feitas uma vez durante a rodada, em qualquer ordem. 

Depois que as ações terminam e o jogador vence a rodada, o próximo jogador inicia sua rodada. Caso o primeiro jogador perca, o outro jogador ganha a partida.
Os critérios de desempate, quando ambas as telas dos jogadores vençam pela regra da paleta, é a grandeza das cartas, sendo o primeiro aspecto considerado os números maiores e o segundo as cores mais altas.  
  
## 4. Referências: 
https://papergames.com.br/red7/

Apresentação das regras do jogo (video do canal Vem Ka Jogar): 

https://www.youtube.com/watch?v=qcX-XYdsKAY
