import re


class Telefones:

    def __init__(self, telefone: str):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("O número de telefone é inválido!")
        if len(telefone) > 13:
            raise ValueError("A quantidade de caracteres está incorreta!")

    def __str__(self) -> str:
        return self.formata_telefone()

    def valida_telefone(self, telefone: str) -> bool:
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def formata_telefone(self) -> str:
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = f"+{resposta.group(1)}({resposta.group(2)})" +\
                           f"{resposta.group(3)}-{resposta.group(4)}"
        numero_formatado_sem_codigo_pais = f"({resposta.group(2)})" + \
                                           f"{resposta.group(3)}-{resposta.group(4)}"
        if resposta.group(1) is None:
            return numero_formatado_sem_codigo_pais
        else:
            return numero_formatado
