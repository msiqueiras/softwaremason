from conta import Conta

def teste_conta_deve_ter_saldo_zero():
    conta_nova = Conta()
    saldo_esperado = 0
    resultado_saldo = conta_nova.saldo

    assert saldo_esperado == resultado_saldo

def teste_conta_deve_ter_extrato_vazio():
    conta_nova = Conta()
    extrato_esperado = []
    resultado_extrato = conta_nova.extrato

    assert extrato_esperado == resultado_extrato

def teste_conta_deve_realizar_deposito_POSITIVO():
    '''
    quantia > 0 happy path
    '''
    conta_nova = Conta()
    quantia = 100
    resposta_esperada = "DEPÓSITO REALIZADO COM SUCESSO"
    resposta_real = conta_nova.deposito(quantia)

    assert resposta_esperada == resposta_real 

# def teste_conta_deve_realizar_deposito_invalido():
#     conta_nova = Conta()
#     quantia = -100
#     resposta_esperada = "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER POSITIVO"
#     resposta_real = conta_nova.deposito(quantia)

#     assert resposta_esperada == resposta_real

def teste_conta_deposito_com_quantia_nao_inteira():
    conta_nova = Conta()
    quantia = 150.40 
    resposta_esperada = "VALOR DE QUANTIA DE DEPÓSITO PRECISA SER INTEIRO"
    resposta_real = conta_nova.deposito(quantia)

    assert resposta_esperada == resposta_real


# def teste_conta_saque(): #mesmas regras de depósito.
#     conta_nova = Conta()
#     quantia = 100
#     resposta_esperada = "SAQUE FEITO COM SUCESSO"
#     resposta_real = conta_nova.saque(quantia)

#     assert resposta_esperada == resposta_real


def teste_conta_saque_com_saldo_insuficiente():
    conta_nova = Conta()
    quantia_deposito = 100
    conta_nova.deposito(quantia_deposito)

    quantia_saque = 150
    resposta_esperada = "SALDO DA CONTA INSUFICIENTE PARA SAQUE"
    resposta_real = conta_nova.saque(quantia_saque)

    assert resposta_real == resposta_esperada


def teste_conta_saque_com_quantia_negativa():
    conta_nova = Conta()
    quantia_deposito = 100
    conta_nova.deposito(quantia_deposito)

    quantia_saque = -10
    resposta_esperada = "VALOR DE QUANTIA DE SAQUE PRECISA SER POSITIVO"
    resposta_real = conta_nova.saque(quantia_saque)

    assert resposta_real == resposta_esperada


def teste_conta_saque_com_quantia_nao_inteira():
    conta_nova = Conta()
    quantia_deposito = 100
    conta_nova.deposito(quantia_deposito)

    quantia_saque = 10.2
    resposta_esperada = "VALOR DE QUANTIA DE SAQUE PRECISA SER INTEIRO"
    resposta_real = conta_nova.saque(quantia_saque)

    assert resposta_real == resposta_esperada


def teste_conta_acesso_historico():
    conta_nova = Conta()
    quantia_deposito = 100
    conta_nova.deposito(quantia_deposito)

    quantia_saque = 50
    conta_nova.saque(quantia_saque)

    historico_esperado = [
        ["DEPÓSITO", 100, 100],
        ["SAQUE", 50, 50]
    ]
    historico_real = conta_nova.getEntradas()

    assert historico_real == historico_esperado