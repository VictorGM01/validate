from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_do_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        meses_do_ano = {
            1: "janeiro", 2: "fevereiro", 3: "março", 4:"abril", 5: "maio",
            6: "junho", 7: "julho", 8: "agosto", 9: "setembro", 10: "outubro",
            11: "novembro", 12: "dezembro"
        }
        mes_cadastro = self.momento_do_cadastro.month
        return meses_do_ano[mes_cadastro]

    def dia_da_semana_cadastro(self):
        dias_da_semana = {
            0: "segunda", 1: "terça", 2: "quarta", 3: "quinta",
            4: "sexts", 5: "sábado", 6: "domingo"
        }
        dia_cadastro = self.momento_do_cadastro.weekday()
        return dias_da_semana[dia_cadastro]

    def data_formatada(self):
        data_formatada = self.momento_do_cadastro.strftime("%d/%m/%Y  %H:%M:%S")
        return data_formatada

    def tempo_de_cadastro(self):
        return datetime.today() - self.momento_do_cadastro
