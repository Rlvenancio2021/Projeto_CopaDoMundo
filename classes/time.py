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
        jogador = input("Digite o nome do jogador").capitalize().strip()
        self.__escalacao.append(jogador)
        Resp = input("Deseja incluir outro jogador? \"S\" ou \"N\"").upper()
        while Resp == "S":
            jogador = input("Digite o nome do jogador").capitalize().strip()
            self.__escalacao.append(jogador)
            Resp = input("Deseja incluir outro jogador? \"S\" ou \"N\"").upper()

    def exclui_jogador(self):
        jogador_a_excluir = input("Digite o jogador(es) que será(ão) escluido(s) da escalação: ").capitalize().strip()
        for jogador in self.__escalacao:
            if jogador_a_excluir == jogador:
                self.__escalacao.remove(jogador)
                resp = "Jogador excluído com sucesso!"
            else:
                resp = "Jogador não está na lista!"
        return resp

    def alterar_tecnico(self):
        novo_tecnico = input("Digite o nome do novo técnico: ").capitalize().strip()
        self.__tecnico = novo_tecnico

    def marca_gol(self):
        nome_do_jogador = input("Qual jogador marcou gol: ").capitalize().strip()
        if nome_do_jogador in self.__escalacao:
            total_gols_marcados = int(input("Quantos gols foram marcados: "))
            self.__artileiro[nome_do_jogador] = total_gols_marcados
            self.__saldo_de_gols += total_gols_marcados
        else:
            print(f'O {nome_do_jogador} não joga neste time')

    def sofre_gol(self):
        gols_sofridos = int(input("Digite a quantidade de gols sofridos: "))
        self.__saldo_de_gols -= gols_sofridos

    def artileiro(self):
        return self.__artileiro