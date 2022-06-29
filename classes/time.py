class Jogador:
    def __init__(self, primeiro_nome, nome_completo):
        self.__primeiro_nome = primeiro_nome.title().strip()
        self.__nome_completo = nome_completo.title().strip()
        self.__gols_marcados = 0
        self.__faltas_cometidas = 0
        self.__faltas_sofridas = 0
        self.__cartoes_recebido = []

        self.__escalacao = {}
        self.__saldo_de_gols = 0

    def inclui_jogador(self, nome):
        jogador = super().__init__(nome)
        self.__escalacao[jogador[0]] = jogador[1]
        return "Jogador incluído com sucesso!"

    def exclui_jogador(self, nome):
        jogador = nome.title().strip()
        if jogador in self.__escalacao.keys():
            self.__escalacao.pop(jogador)
        return "Jogador excluído com sucesso!"

    def jogadores(self):
        for jogador in self.__escalacao.keys():
            print(jogador)

    def marca_gol(self, nome_jogador):
        jogador = nome_jogador.title().strip()
        if jogador in self.__escalacao.keys():
            self.__escalacao[jogador] += 1
            self.__saldo_de_gols += 1
            return "Gol marcado com sucesso!"
        else:
            return "Jogador não é deste time!"

    def anula_gol(self, nome_jogador):
        jogador = nome_jogador.title().strip()
        if jogador in self.__escalacao.keys():
            if self.__escalacao[jogador] > 0:
                self.__escalacao[jogador] -= 1
                self.__saldo_de_gols -= 1
                return "Gol anulado com sucesso!"
            else:
                return "Jogador não tem gol a ser anulado!"
        else:
            return "Jogador não é deste time!"

    def sofre_gol(self):
        self.__saldo_de_gols -= 1
        return "Anotado com sucesso!"