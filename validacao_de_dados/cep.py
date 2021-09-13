# instale a biblioteca requests!
import requests


class BuscaEndereco:

    def __init__(self, cep: str):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self) -> str:
        return self.cep_formatado()

    def valida_cep(self, cep) -> bool:
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_formatado(self) -> str:
        return f"{self.cep[0:5]}-{self.cep[5:]}"

    def acessa_api_cep(self) -> str:
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        get_endereco = requests.get(url)
        dados = get_endereco.json()
        return f"Bairro: {dados['bairro']} - Cidade: " + \
               "{dados['localidade']} - Estado: {dados['uf']}"
