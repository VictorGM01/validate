# precisa instalar o validate-docbr
from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento: str):
        if len(documento) == 11:
            return DocumentoCpf(documento)
        elif len(documento) == 14:
            return DocumentoCnpj(documento)
        else:
            raise ValueError("A quantidade de dígitos é inválida")


class DocumentoCpf:
    def __init__(self, documento: str):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self) -> str:
        return self.formata()


class DocumentoCnpj:
    def __init__(self, documento: str):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self) -> str:
        return self.formata()
