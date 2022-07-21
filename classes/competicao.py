class Competicao():
    def __init__(self, nome_da_competicao):
        self.__nome_da_competicao = nome_da_competicao.title()
        self.__calendario_de_jogos = {"Calendário Geral": []}
        self.__fases_do_jogo = []
        self.__times_participantes = {}

    def inclui_fases_da_competicao(self):
        qtdade_de_fase = int(input("Quantas fases tem nessa competição: "))
        cont = 1
        while cont <= qtdade_de_fase:
            fase = input("Digite o nome da fase: ").title()
            if fase == "":
                print("Por favor, digite um nome válido")
            else:
                self.__fases_do_jogo.append(fase)
                cont += 1
        print("Fase(s) cadastrada(s) com sucesso!")

    def exclui_fase_da_competicao(self):
        fase_a_ser_excluida = input("Digite a fase que deseja excluir: ").title()
        if fase_a_ser_excluida in self.__fases_do_jogo:
            self.__fases_do_jogo.remove(fase_a_ser_excluida)
            print("Fase excluida com sucesso!")
        else:
            print("Fase não identificada!")

    def inclui_calendario_de_jogos(self):
        calendario_por_fase = input("O calendário é dividido por fase? \"S\" ou \"N\"").upper()
        if calendario_por_fase == "S":
            fase = input("Deseja registrar o calendário de jogos de qual fase: ").title()
            if fase in self.__fases_do_jogo:
                fase_escolhida = fase
                data_do_jogo = input("Informe a data que deseja cadastrar: ")
                self.__calendario_de_jogos[fase_escolhida] = [data_do_jogo]
                resp = input("Deseja cadastrar outra data? \"S\" ou \"N\"").upper()
                while resp == "S":
                    data_do_jogo = input("Informe a data que deseja cadastrar: ")
                    self.__calendario_de_jogos[fase_escolhida].append(data_do_jogo)
                    resp = input("Deseja cadastrar outra data? \"S\" ou \"N\"").upper()
                    print()
            else:
                print(f"A fase {fase}, não foi identificada.")
        else:
            data_do_jogo = input("Informe a data que deseja cadastrar: ")

            self.__calendario_de_jogos["Calendário Geral"].append(data_do_jogo)
            resp = input("Deseja cadastrar outra data? \"S\" ou \"N\"").upper()
            while resp == "S":
                data_do_jogo = input("Inform a data que deseja cadastrar: ")
                self.__calendario_de_jogos["Calendário Geral"].append(data_do_jogo)
                resp = input("Deseja cadastrar outra data? \"S\" ou \"N\"").upper()
        print("Calendário cadastrado com sucesso!")

    def exclui_data_do_calendario (self):
        data_a_excluir = input("Informe a data que deseja excluir: ").title()
        if data_a_excluir in self.__calendario_de_jogos["Calendário Geral"]:
            print("encontrado")
            self.__calendario_de_jogos["Calendário Geral"].remove(data_a_excluir)
            print("Data excluída com sucesso!")
        else:
            print("Data não identificada!")

    def inclui_times(self):
        grupo = input("Qual grupo o time pertence: ").title()
        if grupo in self.__times_participantes.keys():
            time = input("Digite o nome do time: ").title()
            while time != "":
                self.__times_participantes[grupo].append(time)
                time = input("Digite o nome do time: ")
                print("Time(s) incluido(s) com sucesso!").title()
        else:
            print(f"O {grupo} não foi encontrado")

    def apresenta_grupos(self):
        print("Os grupos da competição são:")
        for grupo in self.__times_participantes:
            print(grupo)

    def apresenta_time(self):
        print(f"Esses são os times participantes são:")
        for times in self.__times_participantes.values():
            for time in times:
                print(time)

    def apresenta_time_por_grupo(self):
        print("Os times por grupo são:")
        for grupo in self.__times_participantes:
            print(f"{grupo} - {self.__times_participantes[grupo]}")