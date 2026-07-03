# AD141 Python Exercicios

Repositorio publico para armazenar os exercicios do curso
[Red Hat Training Presents: Introduction to Python Programming (AD141)](https://www.redhat.com/pt-br/services/training/ad141-red-hat-training-presents-introduction-to-python-programming).

## Estrutura do repositorio

- `01-basics/`: Capitulo 1, sintaxe basica, entrada/saida, tipos numericos, operadores, strings e conversoes.
- `02-language/`: Capitulo 2, componentes da linguagem, controle de fluxo, operadores logicos e lacos.
- `03-collections/`: Capitulo 3, listas, tuplas, sets, dicionarios e comprehensions.
- `04-functions/`: Capitulo 4, definicao de funcoes, argumentos, escopo, closures e lambdas.
- `05-modules/`: Capitulo 5, criacao e importacao de modulos, namespaces e `sys.argv`.
- `06-classes/`: Capitulo 6, classes, propriedades, metodos especiais, heranca e polimorfismo.
- `07-exceptions/`: Capitulo 7, tratamento de excecoes, try/except, raise, excecoes personalizadas e assert.
- `08-io/`: Capitulo 8, leitura e escrita de arquivos texto/binarios, `open()`, `with`, `seek`/`tell`, `os` e `os.path`.

## Capitulo 1. Basic Python Syntax

### Resumo

Descreve a sintaxe fundamental da linguagem Python e o desenvolvimento de
aplicacoes simples.

### Objetivo

Descrever a sintaxe fundamental da linguagem Python e desenvolver aplicacoes
simples.

### Objetivos de aprendizado

- Usar a sintaxe correta da linguagem Python em programas.
- Usar corretamente funcoes basicas de entrada e saida.
- Escrever programas com tipos numericos padrao e seus operadores.
- Usar strings e seus metodos em programas Python.
- Converter entre tipos numericos e strings.

### Arquivos relacionados

- `01-basics/basics_ex01.py`
- `01-basics/basics_ex02.py`
- `01-basics/basics_ex03.py`
- `01-basics/basics_ex04.py`
- `01-basics/basics_ex05.py`
- `01-basics/basics_ex06.py`
- `01-basics/basics_ex07.py`
- `01-basics/basics_ex08.py`

## Capitulo 2. Language Components

### Resumo

Apresenta estruturas fundamentais de decisao, operadores logicos e estruturas
de iteracao.

### Objetivo

Usar estruturas fundamentais de tomada de decisao, operadores logicos e
instrucoes de iteracao.

### Objetivos de aprendizado

- Usar corretamente a indentacao exigida pelo Python.
- Usar corretamente as estruturas de controle de fluxo.
- Entender e usar operadores relacionais e logicos.
- Usar instrucoes `if` para tomar decisoes no codigo.
- Usar lacos `while` e `for` para operacoes repetitivas.

### Arquivos relacionados

- `02-language/language_ex01.py`
- `02-language/language_ex02.py`
- `02-language/language_ex03.py`
- `02-language/language_ex04.py`
- `02-language/language_ex05.py`
- `02-language/language_ex06.py`
- `02-language/language_ex07.py`
- `02-language/language_ex08.py`

## Capitulo 3. Collections

### Resumo

Apresenta as colecoes nativas do Python: listas, tuplas, sets e dicionarios,
incluindo slicing, concatenacao, operacoes de conjunto e comprehensions.

### Objetivo

Usar listas, tuplas, sets e dicionarios para armazenar e manipular dados.

### Objetivos de aprendizado

- Criar e manipular listas com metodos como `append`, `sort` e slicing.
- Usar tuplas como sequencias imutaveis.
- Usar sets para armazenar valores unicos e operacoes de conjunto.
- Usar dicionarios para mapear chaves a valores.
- Usar comprehensions para construir colecoes de forma concisa.

### Arquivos relacionados

- `03-collections/collections_ex01.py`
- `03-collections/collections_ex02.py`
- `03-collections/collections_ex03.py`
- `03-collections/collections_ex04.py`
- `03-collections/collections_ex05.py`
- `03-collections/collections_ex06.py`

## Capitulo 4. Functions

### Resumo

Apresenta definicao e uso de funcoes, argumentos posicionais e nomeados,
valores padrao, `*args` e `**kwargs`, funcoes aninhadas, closures e lambda.

### Objetivo

Definir e usar funcoes para organizar e reutilizar codigo.

### Objetivos de aprendizado

- Definir funcoes com `def` e retornar valores com `return`.
- Usar argumentos padrao, nomeados e variaveis (`*args`).
- Entender escopo de variaveis locais e globais.
- Criar funcoes aninhadas e closures.
- Usar expressoes lambda para funcoes simples.

### Arquivos relacionados

- `04-functions/functions_ex01.py`
- `04-functions/functions_ex02.py`
- `04-functions/functions_ex03.py`
- `04-functions/functions_ex04.py`
- `04-functions/functions_ex05.py`
- `04-functions/functions_ex06.py`
- `04-functions/functions_ex07.py`
- `04-functions/functions_ex08.py`
- `04-functions/functions_ex09.py`
- `04-functions/functions_ex10.py`
- `04-functions/functions_ex11.py`
- `04-functions/functions_ex12.py`
- `04-functions/functions_ex13.py`

## Capitulo 5. Modules

### Resumo

Apresenta criacao e importacao de modulos, o namespace `__name__`, a guarda
`if __name__ == "__main__"`, e argumentos de linha de comando com `sys.argv`.

### Objetivo

Organizar codigo em modulos e importa-los em outros programas.

### Objetivos de aprendizado

- Criar modulos com funcoes e classes.
- Importar modulos com `import` e `from ... import`.
- Usar `if __name__ == "__main__"` para codigo executavel.
- Acessar argumentos da linha de comando com `sys.argv`.

### Arquivos relacionados

- `05-modules/math_funcs.py`
- `05-modules/alt_math.py`
- `05-modules/modules_ex01.py`
- `05-modules/modules_ex02.py`
- `05-modules/modules_ex03.py`
- `05-modules/modules_ex04.py`

## Capitulo 6. Classes

### Resumo

Apresenta programacao orientada a objetos em Python: definicao de classes,
atributos, metodos, `@property`, metodos especiais (`__str__`, `__eq__`,
`__lt__`, `__gt__`), heranca com `super()` e polimorfismo.

### Objetivo

Criar e usar classes para modelar objetos do mundo real.

### Objetivos de aprendizado

- Definir classes com `class` e inicializar com `__init__`.
- Usar `@property` para getters e setters.
- Implementar metodos especiais (`__str__`, `__eq__`, `__lt__`, `__gt__`).
- Usar heranca com `super()` para estender classes.
- Entender polimorfismo com `isinstance()`.

### Arquivos relacionados

- `06-classes/person.py`
- `06-classes/family.py`
- `06-classes/worker.py`
- `06-classes/classes_ex01.py`
- `06-classes/classes_ex02.py`
- `06-classes/classes_ex03.py`
- `06-classes/classes_ex04.py`

## Capitulo 7. Exceptions

### Resumo

Tratamento de erros em tempo de execucao usando o modelo de excecoes do Python:
try/except, else, finally, raise, excecoes definidas pelo usuario e assert.

### Objetivo

Criar, tratar e lancar excecoes para controlar erros no codigo.

### Objetivos de aprendizado

- Usar o modelo de excecoes do Python.
- Usar `try` e `except` como clausulas basicas de tratamento.
- Entender e usar varias excecoes na hierarquia de excecoes.
- Levantar excecoes no codigo com `raise`.
- Criar e usar excecoes definidas pelo usuario.
- Entender a palavra-chave `assert` e seus beneficios.

### Conceitos principais

| Conceito       | Descricao                                                                        |
| -------------- | -------------------------------------------------------------------------------- |
| `try`/`except` | Bloco que tenta executar codigo e captura excecoes                               |
| `else`         | Executa se nenhuma excecao ocorreu no `try`                                      |
| `finally`      | Executa sempre, haja excecao ou nao                                              |
| `raise`        | Forca o lancamento de uma excecao                                                |
| `assert`       | Verifica condicao; levanta `AssertionError` se falsa                             |
| Hierarquia     | Toda excecao herda de `BaseException`; excecoes de usuario herdam de `Exception` |

### Excecoes comuns

| Excecao             | Quando ocorre                                 |
| ------------------- | --------------------------------------------- |
| `ValueError`        | Conversao de tipo invalida (ex: `int("abc")`) |
| `IndexError`        | Indice fora dos limites de uma sequencia      |
| `KeyError`          | Chave inexistente em um dicionario            |
| `ZeroDivisionError` | Divisao por zero                              |
| `EOFError`          | Fim de arquivo inesperado (Ctrl+D)            |
| `KeyboardInterrupt` | Interrupcao do usuario (Ctrl+C)               |
| `FileNotFoundError` | Arquivo inexistente                           |
| `TypeError`         | Operacao em tipo inadequado                   |

### Arquivos relacionados

- `07-exceptions/exceptions_ex01.py`
- `07-exceptions/exceptions_ex02.py`
- `07-exceptions/exceptions_ex03.py`

## Capitulo 8. Input and Output

### Resumo

Leitura e escrita de arquivos texto e binarios, streams padrao (`sys.stdin`,
`sys.stdout`, `sys.stderr`), modos de abertura, gerenciamento de contexto
(`with`), acesso aleatorio (`seek`/`tell`), e manipulacao de arquivos e
diretorios com `os` e `os.path`.

### Objetivo

Ler e escrever sequencias de bytes em fluxos de dados de entrada e saida.

### Objetivos de aprendizado

- Usar capacidades adicionais de E/S alem de `input()` e `print()`.
- Criar e usar data streams para ler e escrever arquivos.
- Ler e escrever arquivos de texto.
- Usar `bytes` e `bytearray` para ler e escrever arquivos binarios.
- Usar `seek()` e `tell()` para acesso aleatorio ao conteudo do stream.
- Usar os modulos `os` e `os.path` para trabalhar com arquivos e diretorios.

### Arquivos relacionados

- `08-io/names_a.txt`
- `08-io/names_b.txt`
- `08-io/names_c.txt`
- `08-io/names_d.txt`
- `08-io/io_ex01.py`
- `08-io/io_ex02.py`
- `08-io/io_ex03.py`
- `08-io/io_ex04.py`
- `08-io/io_ex05.py`
- `08-io/io_ex06.py`
- `08-io/io_ex07.py`
- `08-io/io_ex08.py`

## Como executar

Os scripts podem ser executados individualmente. Exemplo:

```bash
python3 01-basics/basics_ex01.py
```
