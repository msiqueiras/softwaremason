# O mínimo que você deveria saber sobre testes unitários

Testes unitários são testes feitos para testar pequenos componentes de um todo. Esses componentes são indivisíveis e devem ser testados de modo a fornecer uma determinada entrada e verificar se a saída resultante é igual ao que era esperado.

* System Under Test (SUT): é o componente em si que será testado na ocasiã, seja uma função, seja uma classe com seus métodos.

## Taxonomia de um teste unitário

1. AAA: Arrange: preparação dos dados e do ambiente necessário para testes / Act: execução da função ou do método que está sendo testado / Assert: validação, onde se compara o resultado obtido com o que deveria ter sido gerado
2. 4 fases: Setup / Exercise / Verify / TearDown 


### Formato ideal de nome de teste (python & pytest)

```bash
def test_<nome_do_SUT>_<oq_ele_deveria_fazer>():
```

### Boas práticas de testes

1. Hardcoded -> justamente para saber onde foi e o que foi que falhou
2. 