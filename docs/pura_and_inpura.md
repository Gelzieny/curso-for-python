# Funções Puras em Python

## O que são Funções Puras?

Uma **função pura** é uma função que sempre retorna o mesmo resultado para os mesmos argumentos e **não causa efeitos colaterais**. Elas são um conceito fundamental na **programação funcional**, pois tornam o código mais previsível, testável e reutilizável.


## Características das Funções Puras

✅ **Determinística**: Sempre retorna o mesmo resultado para os mesmos argumentos.

✅ **Sem efeitos colaterais**: Não modifica variáveis globais, arquivos, banco de dados, etc.

✅ **Imutabilidade**: Não altera os valores de entrada.


## Exemplo de Função Pura
```python
def somar(a, b):
    return a + b  # Apenas retorna um valor, sem modificar nada fora da função

print(somar(3, 5))  # Sempre retornará 8
```
📌 **Por que é pura?**  
- Para `a=3` e `b=5`, sempre retorna `8`.  
- Não altera nada fora dela.


## Exemplo de Função **Não Pura**
```python
total = 0  # Variável global

def somar_e_atualizar(a, b):
  global total
  total += a + b  # Modifica um estado externo (efeito colateral)
  return total

print(somar_e_atualizar(3, 5))  # Saída: 8
print(somar_e_atualizar(3, 5))  # Saída: 16 (resultado diferente!)
```
📌 **Por que não é pura?**  
- Depende de `total`, que pode mudar.
- O retorno não é sempre o mesmo para os mesmos argumentos.




