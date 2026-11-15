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