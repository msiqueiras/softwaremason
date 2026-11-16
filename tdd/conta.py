import logging

class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, quantia: int):
        if quantia <= 0:
            return "VALOR DE QUANTIA PRECISA SER POSITIVO"

        if not isinstance(quantia, int):
            return "VALOR DE QUANTIA PRECISA SER INTEIRO"

        self.saldo += quantia
        self.extrato.append(["DEPÓSITO", quantia, self.saldo])
        return "DEPÓSITO REALIZADO COM SUCESSO"
    