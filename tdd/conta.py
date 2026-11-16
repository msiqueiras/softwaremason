class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def deposito(self, quantia: int):
        if isinstance(quantia, bool) or not isinstance(quantia, int):
            return "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER INTEIRO"

        if quantia <= 0:
            return "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER POSITIVO"

        self.saldo += quantia
        self.extrato.append(["DEPÓSITO", quantia, self.saldo])
        return "DEPÓSITO REALIZADO COM SUCESSO"

    def saque(self, quantia: int):
        if isinstance(quantia, bool) or not isinstance(quantia, int):
            return "VALOR DE QUANTIA DE SAQUE PRECISA SER INTEIRO"
        
        if quantia <= 0:
            return "VALOR DE QUANTIA DE SAQUE PRECISA SER POSITIVO"
        

        if self.saldo < quantia:
            return "SALDO DA CONTA INSUFICIENTE PARA SAQUE"
        
        self.saldo -= quantia
        self.extrato.append(["SAQUE", quantia, self.saldo])
        return "SAQUE FEITO COM SUCESSO"

    def getEntradas(self):
        return self.extrato
    
    