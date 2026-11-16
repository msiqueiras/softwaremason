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
#     resposta_esperada = "VALOR DE QUANTIA PRECISA SER POSITIVO"
#     resposta_real = conta_nova.deposito(quantia)

#     assert resposta_esperada == resposta_real

def teste_conta_deposito_com_quantia_nao_inteira():
    conta_nova = Conta()
    quantia = 150.40 #caso não fosse um número, o python vai reclamar na função
    resposta_esperada = "VALOR DE QUANTIA PRECISA SER INTEIRO"
    resposta_real = conta_nova.deposito(quantia)

    assert resposta_esperada == resposta_real


def teste_conta_saque(): #mesmas regras de depósito.
    conta_nova = Conta()
    quantia = 100
    resposta_esperada = "SAQUE FEITO COM SUCESSO"
    resposta_real = conta_nova.saque(quantia)

    assert resposta_esperada == resposta_real

    