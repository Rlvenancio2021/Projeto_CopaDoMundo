class Jogador:
    def __init__(self, nome, time):
        self.__nome = nome.title().strip()
        self.__time = time.title().strip()
        self.__gols_marcados = 0

    def altera_nome_jogador(self, novo_nome):
        self.__nome = novo_nome.title().strip()

    def altera_time(self, novo_time):
        self.__time = novo_time.title().strip()

    def marca_gol(self):
        self.__gols_marcados += 1
        return "Gol anotado com sucesso!"

    def anula_gol(self):
        self.__gols_marcados -= 1
        return "Gol anulado com sucesso!"

    def dados_jogador(self):
        jogador = {self.__nome:[self.__time, self.__gols_marcados]}
        return jogador

class Time:
    def __init__(self):
        self.__nome_do_time = input("Digite o nome do time: ").capitalize().strip()
        self.__tecnico = input("Digite o nome do técnico: ").capitalize().strip()
        self.__escalacao = []
        self.__saldo_de_gols = 0
        self.__artileiro = {}

    def apresenta_time(self):
        return print(
            f"Apresento o time {self.__nome_do_time}, "
            f"seu técino o sr(a) {self.__tecnico}, "
            f"e os jogadores {self.__escalacao}, "
            f"o saldo de gols do time é {self.__saldo_de_gols}, "
            f"os jogadores que marcaram gol foram {self.__artileiro}"
        )

    def dados_do_time(self):
        dados_do_time = {}
        dados_do_time[self.__nome_do_time] = self.__escalacao
        return dados_do_time

    def inclui_jogadores(self):
        validacao1 = input("Sabe quantos jogadores serão cadastrado? \"S\" ou \"N\"").upper()
        if validacao1=="S":
            quantidade = int(input("Quantos jogadores serão inseridos:"))
            cont = 0
            while quantidade > cont:
                jogador = input("Digite o nome do jogador").capitalize().strip()
                while jogador == "":
                    print("Favor digitar um nome válido!")
                    jogador = input("Digite o nome do jogador").capitalize().strip()
                self.__escalacao.append(jogador)
                cont += 1
        else:
            jogador = input("Digite o nome do jogador").capitalize().strip()
            while jogador == "":
                print("Favor digitar um nome válido!")
                jogador = input("Digite o nome do jogador").capitalize().strip()
            self.__escalacao.append(jogador)
            Resp = input("Deseja incluir outro jogador? \"S\" ou \"N\"").upper()
            while Resp == "S":
                jogador = input("Digite o nome do jogador").capitalize().strip()
                while jogador == "":
                    print("Favor digitar um nome válido!")
                    jogador = input("Digite o nome do jogador").capitalize().strip()
                self.__escalacao.append(jogador)
                Resp = input("Deseja incluir outro jogador? \"S\" ou \"N\"").upper()

    def exclui_jogador(self):
        jogador_a_excluir = input("Digite o jogador que será excluído do time: ").capitalize().strip()
        if jogador_a_excluir in self.__escalacao:
            self.__escalacao.remove(jogador_a_excluir)
            return "Jogador excluído com sucesso!"
        else:
            return "Jogador não está na lista!"

    def alterar_tecnico(self):
        novo_tecnico = input("Digite o nome do novo técnico: ").capitalize().strip()
        self.__tecnico = novo_tecnico

    def marca_gol(self):
        nome_do_jogador = input("Qual jogador marcou gol: ").capitalize().strip()
        if nome_do_jogador in self.__escalacao:
            total_gols_marcados = int(input(f"Quantos gols {nome_do_jogador} marcou nesse jogo: "))
            self.__artileiro[nome_do_jogador] = total_gols_marcados
            self.__saldo_de_gols += 1
        else:
            print(f'O {nome_do_jogador} não joga neste time')

    def sofre_gol(self):
        gol_sofrido = 1
        self.__saldo_de_gols -= gol_sofrido

    def artileiro(self):
        return self.__artileiro