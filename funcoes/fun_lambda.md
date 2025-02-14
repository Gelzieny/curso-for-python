# Função Lambda em Python

Uma **função lambda** é uma **função anônima e curta** que pode ter múltiplos argumentos, mas apenas uma **expressão**. Elas são úteis para operações simples e rápidas, sem a necessidade de definir uma função tradicional com `def`.

### **Sintaxe da Função Lambda**
```python
lambda argumentos: expressão
```

### **Exemplo de Função Lambda**
```python
soma = lambda x, y: x + y

print(soma(3, 5))  # Saída: 8
```

### **Uso com `map()`, `filter()` e `sorted()`**

#### `map()` - Aplicar uma função a cada item da lista
```python
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))

print(dobrados)  # Saída: [2, 4, 6, 8]
```

#### `filter()` - Filtrar valores com base em uma condição
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6]
```

#### `sorted()` - Ordenação personalizada
```python
palavras = ["banana", "maçã", "uva", "abacaxi"]
ordenadas = sorted(palavras, key=lambda palavra: len(palavra))

print(ordenadas)  # Saída: ['uva', 'maçã', 'banana', 'abacaxi']
```
