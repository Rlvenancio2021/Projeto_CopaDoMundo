from classes.time import Time

class Competicao():
    def __init__(self, nome_da_competicao):
        self.__nome_da_competicao = nome_da_competicao.title()
        self.__calendario_de_jogos = {"Calendário Geral": []}
        self.__fases_do_jogo = []


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