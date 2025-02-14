# Subprogramas em Funções

- **Funções auxiliares**: São funções menores que são chamadas dentro de outras funções para executar uma tarefa específica. Elas ajudam a tornar o código mais modular e reutilizável.

- **Funções recursivas**: Uma função que chama a si mesma. Elas podem ser usadas para resolver problemas que podem ser divididos em subproblemas menores e semelhantes ao problema original, como o cálculo de fatorial ou a busca em uma árvore binária.

### Exemplo de função auxiliar:

```python
def somar(a, b):
   return a + b

def calcular_media(lista):
   total = 0
   for num in lista:
      total = somar(total, num)  # chamando a função auxiliar somar
   return total / len(lista)

# Exemplo de uso
media = calcular_media([10, 20, 30])
print(media)
```

Exemplo de função recursiva (cálculo do fatorial):

```python
def fatorial(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * fatorial(n - 1)  # chamada recursiva

# Exemplo de uso
resultado = fatorial(5)
print(resultado)
```
Esses subprogramas ajudam a tornar o código mais organizado, eficiente e fácil de manter.