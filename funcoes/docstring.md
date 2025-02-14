# Docstrings em Funções

### 📌 Por que usar docstrings?

* Melhor compreensão do código.
* Facilita a manutenção e colaboração em projetos.
* Permite gerar documentação automaticamente com ferramentas como Sphinx.
* Pode ser acessada diretamente com `help(funcao)` ou `funcao.__doc__`.

#### 🔹 Exemplo de Docstring Simples

````py
def somar(a, b):
  """Retorna a soma de dois números."""
  return a + b

# Acessando a docstring
print(somar.__doc__)
````
Saída:

````bash
Retorna a soma de dois números.
````

#### 🔹 Exemplo de Docstring Padrão com Descrição Completa

````py
def calcular_media(lista):
  """
  Calcula a média de uma lista de números.

  Parâmetros:
  lista (list): Uma lista contendo números inteiros ou decimais.

  Retorna:
  float: A média dos números na lista.

  Exemplo:
  >>> calcular_media([10, 20, 30])
  20.0
  """
  total = sum(lista)
  return total / len(lista) if lista else 0
````

#### 🔹 Exemplo de Docstring para Função Recursiva

````py
def fatorial(n):
  """
  Calcula o fatorial de um número inteiro não negativo.

  Parâmetros:
  n (int): Número para calcular o fatorial. Deve ser um inteiro positivo ou zero.

  Retorna:
  int: O fatorial de n.

  Exemplo:
  >>> fatorial(5)
  120
  """
  if n == 0 or n == 1:
    return 1
  return n * fatorial(n - 1)
````
#### 🔹 Como Exibir Docstrings no Terminal

Você pode visualizar a docstring de uma função usando o comando `help()`:
````bash
help(calcular_media)
````

Ou acessando diretamente:
````bash
print(calcular_media.__doc__)
````

#### 🚀 Boas Práticas ao Escrever Docstrings
    ✔ Seja claro e objetivo.
    ✔ Use frases curtas e diretas.
    ✔ Inclua detalhes sobre os parâmetros e valores de retorno.
    ✔ Utilize exemplos quando necessário.
    ✔ Siga padrões de documentação como PEP 257.