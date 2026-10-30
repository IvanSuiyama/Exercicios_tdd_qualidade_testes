# Exercícios de TDD — Qualidade de Software

Implementação, em **Python**, dos três exercícios da lista de **TDD** da disciplina de
Qualidade de Software, seguindo a técnica de *Test Driven Development*: os testes
descrevem o comportamento esperado e o código de produção é escrito para atendê-los.

| Exercício | Tema | Módulo | Testes |
|---|---|---|---|
| 1 | Classificação de triângulos | `exercicio1_triangulo/` | 29 |
| 2 | `PersonDAO.isValidToInclude()` | `exercicio2_person/` | 34 |
| 3 | Calculadora de salário | `exercicio3_salario/` | 25 |
| | **Total** | | **88** |

---

## Tecnologias

- **Python 3.13** (compatível com 3.10+, por causa da sintaxe `int | None`)
- **pytest** — framework de testes adotado (a lista permite `unittest` ou `pytest`)
- **pytest-cov** — evidência de cobertura de código por teste
- **Decimal** — aritmética monetária sem erro de ponto flutuante

---

## Estrutura do projeto

```
.
├── exercicio1_triangulo/
│   ├── __init__.py
│   ├── triangulo.py
│   └── tests/
│       ├── __init__.py
│       └── test_triangulo.py
├── exercicio2_person/
│   ├── __init__.py
│   ├── email.py
│   ├── person.py
│   ├── person_dao.py
│   └── tests/
│       ├── __init__.py
│       └── test_person_dao.py
├── exercicio3_salario/
│   ├── __init__.py
│   ├── cargo.py
│   ├── funcionario.py
│   ├── calculadora_salario.py
│   └── tests/
│       ├── __init__.py
│       └── test_calculadora_salario.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md
```

Cada exercício é um pacote Python independente, com o código de produção na raiz do
pacote e os testes no subpacote `tests/`.

### Arquivos de apoio

- **`requirements.txt`** — declara as dependências do projeto (`pytest` e `pytest-cov`)
  com as versões mínimas. É o que torna o *build* reproduzível: em vez de versionar o
  ambiente virtual, versiona-se a receita para recriá-lo.
- **`pytest.ini`** — configuração do pytest. Define a raiz do projeto (`rootdir`), quais
  pastas são varridas quando não se passa argumento (`testpaths`), a convenção de nome
  dos testes (`python_files`), a raiz no `sys.path` para os imports dos pacotes
  (`pythonpath`) e as flags aplicadas a toda execução (`addopts`).
- **`conftest.py`** — ponto de extensão do pytest para fixtures e hooks compartilhados,
  carregado automaticamente antes da coleta. No estado atual é opcional: cada arquivo de
  teste define as próprias fixtures e o `pythonpath` do `pytest.ini` já resolve os
  imports.
- **`Makefile`** — atalhos para os comandos do projeto (`make test`, `make coverage`),
  para que os procedimentos descritos neste README sejam executáveis sem depender de
  comandos longos digitados à mão. Não é exigido pela tarefa; é conveniência.
- **`.gitignore`** — impede o versionamento de artefatos gerados (`.venv/`,
  `__pycache__/`, `.pytest_cache/`, `htmlcov/`, `.coverage/`) e de materiais pessoais.

---

## Pré-requisitos

- Python 3.10 ou superior
- `pip` e `venv`

Verifique com:

```bash
python3 --version
```

---

## Build (instalação das dependências)

Na raiz do repositório:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Ou, usando o `Makefile`:

```bash
make install
```

> Não há etapa de compilação: sendo Python, o *build* consiste em criar o ambiente
> virtual e instalar as dependências de teste declaradas em `requirements.txt`.

---

## Execução dos testes

Todos os exercícios:

```bash
pytest
```

Um exercício específico:

```bash
pytest exercicio1_triangulo
pytest exercicio2_person
pytest exercicio3_salario
```

Via `Makefile`:

```bash
make test        # todos
make test-ex1    # apenas o Exercício 1
make test-ex2    # apenas o Exercício 2
make test-ex3    # apenas o Exercício 3
```

Resultado esperado:

```
88 passed
```

---

## Cobertura de código por teste

A evidência de cobertura é gerada com **pytest-cov**. Para cada exercício, rode:

```bash
pytest <exercicio> --cov=<exercicio> --cov-report=term-missing --cov-report=html:htmlcov/<exercicio>
```

ou simplesmente:

```bash
make coverage           # relatório no terminal + HTML por exercício
make coverage-all       # relatório consolidado do projeto inteiro
```

O relatório HTML fica em `htmlcov/<exercicio>/index.html` (pasta ignorada pelo Git;
os números comprovando a cobertura estão reproduzidos abaixo).

### Evidência — Exercício 1 (Triângulo)

```text
$ pytest exercicio1_triangulo --cov=exercicio1_triangulo --cov-report=term-missing

29 passed

Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
exercicio1_triangulo/__init__.py                   0      0   100%
exercicio1_triangulo/tests/__init__.py             0      0   100%
exercicio1_triangulo/tests/test_triangulo.py      37      0   100%
exercicio1_triangulo/triangulo.py                 30      0   100%
----------------------------------------------------------------------------
TOTAL                                             67      0   100%
```

### Evidência — Exercício 2 (Person / Email / PersonDAO)

```text
$ pytest exercicio2_person --cov=exercicio2_person --cov-report=term-missing

34 passed

Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
exercicio2_person/__init__.py                    0      0   100%
exercicio2_person/email.py                       6      0   100%
exercicio2_person/person.py                      9      0   100%
exercicio2_person/person_dao.py                 45      0   100%
exercicio2_person/tests/__init__.py              0      0   100%
exercicio2_person/tests/test_person_dao.py      75      0   100%
--------------------------------------------------------------------------
TOTAL                                          135      0   100%
```

### Evidência — Exercício 3 (Calculadora de salário)

```text
$ pytest exercicio3_salario --cov=exercicio3_salario --cov-report=term-missing

25 passed

Name                                                   Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------------
exercicio3_salario/__init__.py                             0      0   100%
exercicio3_salario/calculadora_salario.py                 22      0   100%
exercicio3_salario/cargo.py                                6      0   100%
exercicio3_salario/funcionario.py                         18      0   100%
exercicio3_salario/tests/__init__.py                       0      0   100%
exercicio3_salario/tests/test_calculadora_salario.py      61      0   100%
------------------------------------------------------------------------------------
TOTAL                                                    107      0   100%
```

### Resumo da cobertura

| Exercício | Declarações (stmts) | Cobertas | Cobertura |
|---|---|---|---|
| 1 — Triângulo | 67 | 67 | **100%** |
| 2 — PersonDAO | 135 | 135 | **100%** |
| 3 — Calculadora | 107 | 107 | **100%** |

---

## Exercício 1 — Triângulo

**Enunciado:** ler três valores inteiros que representam os lados de um triângulo e
informar se formam um triângulo isósceles, escaleno ou equilátero.

**Condição de existência:** a soma de dois lados deve ser maior que o terceiro.

### Esqueleto da classe

```python
class Triangulo:
    EQUILATERO = "EQUILATERO"
    ISOSCELES = "ISOSCELES"
    ESCALENO = "ESCALENO"

    @classmethod
    def classificar(cls, lado_a: int, lado_b: int, lado_c: int) -> str:
        ...
```

`classificar()` devolve uma das três constantes. Entradas inválidas geram exceções:

| Situação | Exceção |
|---|---|
| Lado não inteiro (string, float, `None`, `bool`) | `TypeError` |
| Lado zero ou negativo | `ValueError` |
| Soma de dois lados ≤ terceiro lado | `ValueError` |

### Casos de teste implementados

| Item do enunciado | Caso de teste |
|---|---|
| 2.1 | Escaleno válido — `(3, 4, 5)` |
| 2.2 | Isósceles válido — `(5, 5, 7)` |
| 2.3 | Equilátero válido — `(6, 6, 6)` |
| 2.4 | Isósceles com permutação — `(3, 3, 4)`, `(3, 4, 3)`, `(4, 3, 3)` |
| 2.5 | Um valor zero — `(0, 4, 5)`, `(4, 0, 5)`, `(4, 5, 0)` |
| 2.6 | Um valor negativo — `(-1, 4, 5)`, `(4, -1, 5)`, `(4, 5, -1)` |
| 2.7 e 2.8 | Soma igual ao terceiro — as 6 permutações de `(1, 2, 3)` |
| 2.9 e 2.10 | Soma menor que o terceiro — as 6 permutações de `(1, 2, 4)` |
| 2.11 | Três valores iguais a zero — `(0, 0, 0)` |

---

## Exercício 2 — `Person`, `Email` e `PersonDAO`

**Enunciado:** implementar `isValidToInclude()` usando TDD, retornando uma lista de
erros de validação do objeto `Person`.

### Diagrama de classes

```
┌────────────────────┐          ┌──────────────────────┐
│      Person        │          │      PersonDAO       │
├────────────────────┤          ├──────────────────────┤
│ - id: int          │          │ + save(p: Person)    │
│ - name: String     │          │ + isValidToInclude(  │
│ - age: int         │          │     p: Person)       │
└─────────┬──────────┘          │     : List<String>   │
          │ 1                   └──────────────────────┘
          │ possui
          │ 1..*
┌─────────┴──────────┐
│       Email        │
├────────────────────┤
│ - id: int          │
│ - name: String     │
└────────────────────┘
```

Em Python, o atributo de associação 1..* é a lista `Person.emails`.

### Regras de validação

| Regra | Mensagem de erro |
|---|---|
| Nome com ao menos 2 partes | `O nome deve ser composto por ao menos 2 partes.` |
| Nome apenas com letras | `O nome deve ser composto apenas por letras.` |
| Idade no intervalo `[1, 200]` | `A idade deve estar entre 1 e 200.` |
| Idade precisa ser inteira | `A idade deve ser um número inteiro.` |
| Pelo menos um `Email` associado | `O objeto Person deve ter pelo menos um Email associado.` |
| Email no formato `_____@____._____` | `O nome do Email '...' deve estar no formato '_____@____._____'.` |

O método devolve **todos** os erros encontrados (lista vazia quando a pessoa é válida),
e não apenas o primeiro.

### Casos de teste implementados

- Pessoa totalmente válida → lista vazia
- Limites da idade: `1` e `200` válidos; `0`, `-1`, `201` e `1000` inválidos
- Idade não inteira: `"30"`, `30.5`, `None`
- Nome com uma parte, vazio ou só espaços
- Nome com números ou símbolos (`"Ivan 2"`, `"Ivan @Suiyama"`, ...)
- Nome com três partes (válido)
- Pessoa sem nenhum email
- Emails fora do formato: sem `@`, sem ponto, parte vazia antes/depois do `@`,
  parte final vazia, espaço, dois `@`, nome nulo
- Vários emails válidos; um inválido entre válidos (gera exatamente 1 erro)
- `save()`: persiste pessoa válida, recusa inválida com `ValueError` e sobrescreve
  o registro quando o `id` se repete

---

## Exercício 3 — Calculadora de salário

**Enunciado:** calculadora de salário de funcionários. Um funcionário contém nome,
email, salário-base e cargo; o desconto do salário líquido depende do cargo.

### Classes

| Classe | Responsabilidade |
|---|---|
| `Cargo` (`Enum`) | `DESENVOLVEDOR`, `DBA`, `TESTADOR`, `GERENTE` |
| `Funcionario` | nome, email, salário-base (`Decimal`) e cargo |
| `CalculadoraSalario` | `calcular_salario_liquido(funcionario) -> Decimal` |

### Regras de desconto

| Cargo | Salário-base | Desconto |
|---|---|---|
| DESENVOLVEDOR | ≥ 3.000,00 | 20% |
| DESENVOLVEDOR | < 3.000,00 | 10% |
| DBA | ≥ 2.000,00 | 25% |
| DBA | < 2.000,00 | 15% |
| TESTADOR | ≥ 2.000,00 | 25% |
| TESTADOR | < 2.000,00 | 15% |
| GERENTE | ≥ 5.000,00 | 30% |
| GERENTE | < 5.000,00 | 20% |

### Casos de teste implementados

Para **cada** cargo são testados: o valor exato do piso (inclusivo, `>=`), um centavo
abaixo do piso, um valor bem acima e um valor baixo. Exemplos:

| Cargo | Salário-base | Salário líquido |
|---|---|---|
| DESENVOLVEDOR | 3.000,00 | 2.400,00 |
| DESENVOLVEDOR | 2.999,99 | 2.699,99 |
| DBA | 2.000,00 | 1.500,00 |
| DBA | 1.999,99 | 1.699,99 |
| TESTADOR | 2.500,00 | 1.875,00 |
| GERENTE | 5.000,00 | 3.500,00 |
| GERENTE | 4.999,99 | 3.999,99 |

Também são cobertos: conversão de `int`, `float` e `str` para `Decimal`,
arredondamento *half-up* em duas casas, salário-base negativo (`ValueError`),
cargo sem regra cadastrada (`ValueError`) e parâmetro que não é `Funcionario`
(`TypeError`).

---

## Decisões de implementação

- **Nomes em `snake_case`.** `isValidToInclude()` do diagrama virou
  `PersonDAO.is_valid_to_include()`, seguindo a convenção da linguagem adotada
  (PEP 8); o comportamento é o mesmo.
- **Lista de erros como `list[str]`.** Equivale ao `List<String>` do diagrama.
- **`Decimal` para dinheiro.** Evita erros de arredondamento de `float`; o resultado
  é sempre quantizado em 2 casas com `ROUND_HALF_UP`.
- **Entradas inválidas geram exceções.** Em vez de retornar `None`/string mágica, os
  erros de entrada são sinalizados com `ValueError`/`TypeError`, o que deixa os testes
  explícitos e o contrato da API claro.
- **Validação concentrada no `PersonDAO`.** `Person` e `Email` são apenas estruturas
  de dados (dataclasses), como no diagrama; as regras ficam no DAO.
- **`notas.md` e `diagrama.png` não fazem parte da entrega** e estão no `.gitignore`.
