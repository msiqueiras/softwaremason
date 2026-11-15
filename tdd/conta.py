class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, quantia: int):
        self.saldo += quantia
        return "DEPÓSITO REALIZADO COM SUCESSO"
    