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

1. Hardcoded -> justamente para saber onde foi e o que foi que falhou.

## Covarage (cobertura)

É uma métrica utilizada para saber a porcentagem do código que foi executado nos testes automatizados. Ela serve para mapear pontos não executados por aquele teste em especial, identificando pontos cegos e possíveis falhas. Existem alguns tipos de coberturas:

1. Line coverage
2. Statement covarage
3. Branch covarage
4. Function covarage

No python, podemos verificar a cobertura de um teste rodando:

```bash
poetry run pytest <nome_do_teste> -v --cov=<arquivo_de_cobertura> #normalmente é onde está o SUT
```

Podemos ver um report específico do arquivpo executando `covarage html` que gera um arquivo de hmtl mostrando quais partes daquele código foram ou não executadas naquele teste.

## Tipos de testes

* Behaviour - Testes de comportamento que focam em verificar como uma determinada funcionalidade está se comportando diante a um input;
* Structural - Testes de esquema buscam validar um formato de um objeto, para preservar sua estrutura, seus campos, seus tipos de dados e seus atributos. É útil para garantir que, se alguém alterar a modelagem de uma classe ou interface, o sistema identifique a mudança na estrutura original.
* DOC - Teste que depende de outros componentes necessariamente para o seu funcionamento. Testes, aqui, são mais complexos por termos que analisar se o problema é advindo do objeto de dependência ou é interno
* 