# Programa Copo do Mundo

### Como este projeto foi desenvolvido

1°Desenvolvido em Python usando VSCode

2° Escopo do projeto
Montar um programa para acompanhamento da Copa do Mundo de 2022. Engloba acompanhar classificação, artileiro da competição. Fora do escopo acompanhar faltas sofrida e cometida, assistências, cartões amarelo e/ou vermelho, posição dos jogadores (goleiro, zagueiro, etc...).

3° Estrutura do projeto
Primeiro montei um roteiro com todos os requisitos que o programa deveria ter, pensando nas características mais basicas que uma competição (times e jogadores e seus técnicos, classificação por cada fase do campeonato, artileiro)

4° Requisito
No total são 32 times envolvidos na competição e serão divididos em grupos de 4 times, totalizando 8 Grupos, nomeados pelas letra do alfaneto (A, B, C, D, E, F, G e H).
A competição acontece em **6 etapas**, sendo elas ***Fase de Grupo***, ***Oitavas de Finais***, ***Quartas de Finais***, ***Semifinal***, ***Disputa de 3° lugar*** e ***Final***.

- Fase de grupo (8 Grupos), os times pertecente ao grupo se enfrentam em jogos valendo pontos para o time vencedor e em caso de empates, os dois times que somarem mais pontos passarão para a próxima fase.

- Oitavas de Finais, os grupos são reorganizados em 4 sub-grupos (A-B, C-D, E-F e G-H) ficando com 2 times cada, e a competição é organizada de forma que em cada sub-grupo irá constar o 1° e o 2° colocado classificado da *Fase de grupo*, e o primeiro colocado enfrenta o segundo colocado, e o vencedor de cada confronte passa para a próxima fase. (adicionado uma códificação para melhor ilustrar os enfrentamentos).
    - Estrutura:
        - 1°A vs 2°B (V49)
        - 1°B vs 2°A (V51)
        - 1°C vs 2°D (V50)
        - 1°D vs 2°C (V52)
        - 1°E vs 2°F (V53)
        - 1°F vs 2°E (V55)
        - 1°G vs 2°H (V54)
        - 1°H vs 2°G (V56)

- Quartas de finais, os vencedores de cada sub-grupo se enfrentão, os times classificados na fase anterior irão se enfrentar para disputar a classificação para a próxima fase, da seguinte maneira:
    - Dentro do sub-grupo os times vencedores:
        - V49 vs V50 (V57) (Grupo A-B vs C-D)
        - V51 vs V52 (V59) (Grupo A-B vs C-D)
        - V53 vs V54 (V58) (Grupo E-F vs G-H)
        - V55 vs V56 (V60) (Grupo E-F vs G-H)
        
- Semifinal, os 4 times classificados irão disputar para a próxima fase.
    - Da seguinte forma.
        - V57 vs V58
        - V59 vs V60
        
- Decisão do 3° lugar, os times que perderam na SEMIFINAL irão se enfrentar para disputa de terceiro colocado no campeaonato.

- Final, os times vencedores na SEMIFINAL irão se enfrentar para disputa de primeiro colocado no campeoanto.
    
- Da pontuação da FASE DE GRUPO:
    - Vencedor soma 3 pontos;
    - Empate soma 1 pontos;

- Em caso de empate por ponto, será considerado como critério de desempate o saldo de gol, o número de vitórias (V), empates (E) e derrotas (D).

## O que aprendi com esse projeto

### Programação não é só escrever código

É necessário primeiro organizar as idéias, entender melhor o problema que deseja resolver, detalhar o projeto, definir seu escopo, detalhar as regras de negócio para saber quais elementos serão necessário no projeto e qual o comportamento de cada um deles.

Escolhi esse projeto para testar minhas habilidades de desenvolvedor, na costrução completa de um projeto, desde a identificação de um problema até a construção lógica para sua solução. Escolhi e linguagem Python por ser a que escolhi para trilhar essa fornada e minha idéia inicial é explocar o paradigma de Orientação a Objeto.
