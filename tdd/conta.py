import logging

class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, quantia: int):
        if quantia <= 0:
            return "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER POSITIVO"

        if not isinstance(quantia, int):
            return "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER INTEIRO"

        self.saldo += quantia
        self.extrato.append(["DEPÓSITO", quantia, self.saldo])
        return "DEPÓSITO REALIZADO COM SUCESSO"

    def saque(self, quantia: int):
        if quantia <= 0:
            return "VALOR DE QUANTIA PARA SAQUE PRECISA SER POSITIVO"

        if not isinstance(quantia, int):
            return "VALOR DE QUANTIA PARA SAQUE PRECISA SER INTEIRO"

        if self.saldo < quantia:
            return "SALDO DA CONTA INSUFICIENTE PARA SAQUE"
        
        self.saldo -= quantia
        self.extrato.append(["SAQUE", quantia, self.saldo])
        return "SAQUE FEITO COM SUCESSO"
    