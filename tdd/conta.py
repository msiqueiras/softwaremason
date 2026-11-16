class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, quantia: int):
        if quantia <= 0:
            return "VALOR DE QUANTIA PRECISA SER POSITIVO"

        self.saldo += quantia
        return "DEPÓSITO REALIZADO COM SUCESSO"
    