class Jogador:
    def __init__(self, primeiro_nome, nome_completo):
        self.__primeiro_nome = primeiro_nome.title().strip()
        self.__nome_completo = nome_completo.title().strip()
        self.__gols_marcados = 0
        self.__faltas_cometidas = 0
        self.__faltas_sofridas = 0
        self.__cartoes_recebido = []

    @property
    def dados(self):
        return self.__primeiro_nome, self.__nome_completo, self.__gols_marcados, self.__faltas_cometidas, self.__faltas_sofridas, self.__cartoes_recebido

class Time():
    def __init__(self, nome_do_time, nome_do_tecnico):
        self.__nome_do_time = nome_do_time.title().strip()
        self.__nome_do_tecnico = nome_do_tecnico.title().strip()
        self.__escalacao = {}
        self.__gols_marcados = 0
        self.__gols_sofridos = 0
        self.__saldo_de_gols = 0
        self.__artilheiros = {}

    def novo_tecnico(self, novo_tecnico):
        self.__nome_do_tecnico = novo_tecnico.title().strip()
        return "Técnico alterado com sucesso!"

    def escala_jogador(self, primeiro_nome, nome_completo):
        jogador = Jogador(primeiro_nome, nome_completo)
        self.__escalacao[jogador.dados[0]] = {"Nome": jogador.dados[1], "Gols Marcados": jogador.dados[2], "Faltas Cometidas": jogador.dados[3],
                                              "Faltas Sofridas": jogador.dados[4], "Cartões recebidos": jogador.dados[5]}
        return "Jogador escalado com sucesso!"

    def exclui_jogador(self, primeiro_nome):
        jogador = primeiro_nome.title().strip()
        if jogador in self.__escalacao.keys():
            self.__escalacao.pop(jogador)
            return "Jogador excluído com sucesso!"
        else:
            return "Jogador não está na escalação deste time!"

    def apresenta_jogadores(self):
        for jogador in self.__escalacao.keys():
            print(jogador)

    def marca_gol(self, nome_jogador):
        jogador = nome_jogador.title().strip()
        if jogador in self.__escalacao.keys():
            self.__escalacao[jogador]["Gols Marcados"] += 1
            self.__gols_marcados += 1
            self.__saldo_de_gols += 1
            return "Gol marcado com sucesso!"
        else:
            return "Jogador não está na escalação deste time!"

    def anula_gol(self, nome_jogador):
        jogador = nome_jogador.title().strip()
        if jogador in self.__escalacao.keys():
            if self.__escalacao[jogador]["Gols Marcados"] > 0:
                self.__escalacao[jogador]["Gols Marcados"] -= 1
                self.__gols_marcados -= 1
                self.__saldo_de_gols -= 1
                return "Gol anulado com sucesso!"
            else:
                return "Jogador não tem gol a ser anulado!"
        else:
            return "Jogador não está na escalação deste time!"

    def sofre_gol(self):
        self.__gols_sofridos -= 1
        self.__saldo_de_gols -= 1
        return "Gol sofrido anotado com sucesso!"

    def saldo_de_gols(self):
        return f"O {self.__nome_do_time} marcou {self.__gols_marcados} gols, sofreu {self.__gols_sofridos} gols e possui um saldo de {self.__saldo_de_gols} gols."

    def atualiza_artilheiros(self):
        for jogador in self.__escalacao.keys():
            self.__artilheiros[jogador] = self.__escalacao[jogador]['Gols Marcados']
        return "Atualizado com sucesso!"

    def apresenta_artilheiros(self):
        return self.__artilheiros

    def busca_jogador(self, nome):
        jogador = nome.title().strip()
        if jogador in self.__escalacao.keys():
            print(self.__escalacao[jogador])
        else:
            return f"O jogador {jogador} não está escalado nesse time!"