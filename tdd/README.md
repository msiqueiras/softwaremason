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
