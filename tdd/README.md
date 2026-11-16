# Test-Driven Development - Atividade de Engenharia de Software II

Execução dos testes pela biblioteca Pytest. Para executar em cada etapa, rode o comando: `poetry run pytest conta_teste.py`

## Ciclo 1 - Estado Inicial

### Saldo

```bash
============================================= FAILURES ==============================================
__________________________________ teste_conta_deve_ter_saldo_zero __________________________________

    def teste_conta_deve_ter_saldo_zero():
        conta_nova = Conta()
        saldo_esperado = 0
>       resultado_saldo = conta_nova.saldo
                          ^^^^^^^^^^^^^^^^
E       AttributeError: 'Conta' object has no attribute 'saldo'

conta_teste.py:6: AttributeError
====================================== short test summary info ======================================
FAILED conta_teste.py::teste_conta_deve_ter_saldo_zero - AttributeError: 'Conta' object has no attribute 'saldo'
```

### Extrato

```bash
============================================= FAILURES ==============================================
________________________________ teste_conta_deve_ter_extrato_vazio _________________________________

    def teste_conta_deve_ter_extrato_vazio():
        conta_nova = Conta()
        extrato_esperado = []
>       resultado_extrato = conta_nova.extrato()
                            ^^^^^^^^^^^^^^^^^^
E       AttributeError: 'Conta' object has no attribute 'extrato'

tdd/conta_teste.py:13: AttributeError
====================================== short test summary info ======================================
FAILED tdd/conta_teste.py::teste_conta_deve_ter_extrato_vazio - AttributeError: 'Conta' object has no attribute 'extrato'
```

## Ciclo 2 - Depósito

Método de depósito não existe:
```bash
============================================== ERRORS ===============================================
________________________________ ERROR collecting tdd/conta_teste.py ________________________________
ImportError while importing test module '/home/siqueira/UFPA/graduação/2026.4/Eng_Soft_II/softwaremason/tdd/conta_teste.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.12/importlib/__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tdd/conta_teste.py:1: in <module>
    from conta import Conta, deposito
E   ImportError: cannot import name 'deposito' from 'conta' (/home/siqueira/UFPA/graduação/2026.4/Eng_Soft_II/softwaremason/tdd/conta.py)
====================================== short test summary info ======================================
ERROR tdd/conta_teste.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================= 1 error in 0.08s ==========================================
```

Caso o depósito seja negativo:
```bash
============================================= FAILURES ==============================================
___________________________ teste_conta_deposito_com_quantia_nao_inteira ____________________________

    def teste_conta_deposito_com_quantia_nao_inteira():
        conta_nova = Conta()
        quantia = 150.40 #caso não fosse um número, o python vai reclamar na função
        resposta_esperada = "VALOR DE QUANTIA PRECISA SER INTEIRO"
        resposta_real = conta_nova.deposito(quantia)
    
>       assert resposta_esperada == resposta_real
E       AssertionError: assert 'VALOR DE QUA...A SER INTEIRO' == 'DEPÓSITO REA...O COM SUCESSO'
E         
E         - DEPÓSITO REALIZADO COM SUCESSO
E         + VALOR DE QUANTIA PRECISA SER INTEIRO

tdd/conta_teste.py:42: AssertionError
====================================== short test summary info ======================================
FAILED tdd/conta_teste.py::teste_conta_deposito_com_quantia_nao_inteira - AssertionError: assert 'VALOR DE QUA...A SER INTEIRO' == 'DEPÓSITO REA...O COM SUCESSO'
==================================== 1 failed, 4 passed in 0.05s ====================================
```

Caso o depósito seja não-inteiro:
```bash
============================================= FAILURES ==============================================
___________________________ teste_conta_deposito_com_quantia_nao_inteira ____________________________

    def teste_conta_deposito_com_quantia_nao_inteira():
        conta_nova = Conta()
        quantia = 150.40 #caso não fosse um número, o python vai reclamar na função
        resposta_esperada = "VALOR DE QUANTIA PRECISA SER INTEIRO"
        resposta_real = conta_nova.deposito(quantia)
    
>       assert resposta_esperada == resposta_real
E       AssertionError: assert 'VALOR DE QUA...A SER INTEIRO' == 'DEPÓSITO REA...O COM SUCESSO'
E         
E         - DEPÓSITO REALIZADO COM SUCESSO
E         + VALOR DE QUANTIA PRECISA SER INTEIRO

tdd/conta_teste.py:42: AssertionError
====================================== short test summary info ======================================
FAILED tdd/conta_teste.py::teste_conta_deposito_com_quantia_nao_inteira - AssertionError: assert 'VALOR DE QUA...A SER INTEIRO' == 'DEPÓSITO REA...O COM SUCESSO'
==================================== 1 failed, 3 passed in 0.05s ====================================
```

## Ciclo 3 - Saque

Método de saque não existe:
```bash
============================================= FAILURES ==============================================
_________________________________________ teste_conta_saque _________________________________________

    def teste_conta_saque(): #mesmas regras de depósito.
        conta_nova = Conta()
        quantia = 100
        resposta_esperada = "SAQUE FEITO COM SUCESSO"
>       resposta_real = conta_nova.saque(quantia)
                        ^^^^^^^^^^^^^^^^
E       AttributeError: 'Conta' object has no attribute 'saque'

tdd/conta_teste.py:49: AttributeError
====================================== short test summary info ======================================
FAILED tdd/conta_teste.py::teste_conta_saque - AttributeError: 'Conta' object has no attribute 'saque'
==================================== 1 failed, 4 passed in 0.05s ====================================
```