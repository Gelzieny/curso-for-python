# Funções
Em Python (e em programação de forma geral), parâmetro e argumento são conceitos relacionados, mas distintos:

- `Parâmetro`: É a variável definida na assinatura de uma função que serve como um "espaço reservado" para receber um valor quando a função é chamada.
- `Argumento`: É o valor real passado para a função quando ela é chamada.

### Exemplo:
````py
def saudacao(nome):  # 'nome' é um parâmetro
  print(f"Olá, {nome}!")
    
saudacao("Gelzieny")  # "Gelzieny" é um argumento
````
### 📌 Explicação:

* `nome` é um parâmetro da função saudacao, ou seja, ele define o que a função pode receber.
* `"Gelzieny"` é o argumento, ou seja, o valor passado na chamada da função.

## Tipos de Parâmetros e Argumentos:

1. Parâmetros Posicionais:

````py
def soma(a, b):
  return a + b

resultado = soma(5, 3)  # 5 e 3 são argumentos posicionais
````

* Aqui, `a` e `b` são parâmetros e recebem os valores na ordem em que são passados.


2. Parâmetros Nomeados (Keyword Arguments):

````py
def pessoa(nome, idade):
  print(f"Nome: {nome}, Idade: {idade}")

pessoa(idade=30, nome="Ana")  # Argumentos nomeados
````

* A ordem não importa, pois estamos especificando `nome="Ana"` e `idade=30`.

3. Parâmetros com Valores Padrão:
````py
def apresentar(nome="Visitante"):
  print(f"Bem-vindo, {nome}!")

apresentar()  # Usa o valor padrão "Visitante"
apresentar("Gelzieny")  # Substitui pelo argumento "Gelzieny"
````
* Se nenhum argumento for passado, o parâmetro usa o valor padrão.

4. Parâmetro `*args` (Vários Argumentos Posicionais):

````py
def somar(*numeros):
  return sum(numeros)

print(somar(1, 2, 3, 4, 5))  # Aceita vários argumentos
````
* `*args` permite passar múltiplos argumentos, que são tratados como uma tupla dentro da função.

5. Parâmetro `**kwargs` (Vários Argumentos Nomeados):

````py
def dados_pessoais(**info):
  for chave, valor in info.items():
    print(f"{chave}: {valor}")

dados_pessoais(nome="Maria", idade=25, cidade="São Paulo")
````
* `**kwargs` recebe argumentos nomeados como um dicionário.