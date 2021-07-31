# instale a biblioteca requests!
import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.cep_formatado()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_formatado(self):
        return f"{self.cep[0:5]}-{self.cep[5:]}"

    def acessa_api_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        get_endereco = requests.get(url)
        dados = get_endereco.json()
        print(
            f"Bairro: {dados['bairro']} - Cidade: {dados['localidade']} - Estado: {dados['uf']}"
        )