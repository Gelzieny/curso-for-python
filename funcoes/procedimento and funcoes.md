# Diferença entre Funções e Procedimentos em Python

Em Python, **funções** e **procedimentos** são blocos de código reutilizáveis, mas diferem no objetivo principal:

## 1. O que são Funções?
Uma **função** é um bloco de código que realiza uma tarefa específica e **retorna um valor** usando a palavra-chave `return`. 

### Exemplo de Função:
```python
# Função que soma dois números e retorna o resultado
def soma(a, b):
    return a + b  # Retorna um valor

resultado = soma(5, 3)
print(resultado)  # Saída: 8
```

### Características:
- **Retornam um valor** utilizando `return`.
- Podem ser usadas dentro de expressões, atribuídas a variáveis ou passadas como argumentos.
- Melhoram a reutilização e modularização do código.

## 2. O que são Procedimentos?
Um **procedimento** é uma função que **não retorna um valor explícito**, ou seja, pode executar ações, mas retorna `None` por padrão.

### Exemplo de Procedimento:
```python
# Procedimento que exibe uma mensagem na tela
def exibir_mensagem(nome):
    print(f"Olá, {nome}!")  # Apenas exibe uma mensagem

exibir_mensagem("Gelzieny")  # Saída: Olá, Gelzieny!
```

### Características:
- **Não retornam valores explícitos** (retornam `None` por padrão).
- São usados para **efeitos colaterais**, como imprimir na tela ou modificar arquivos.

## 3. Comparando Funções e Procedimentos
| Característica  | Função | Procedimento |
|---------------|--------|-------------|
| **Usa `return`?** | Sim | Não (ou retorna `None`) |
| **Pode armazenar o retorno?** | Sim | Não |
| **Objetivo** | Processar e retornar dados | Executar uma ação |
| **Exemplo** | `def soma(a, b): return a + b` | `def exibir(): print("Olá")` |

## 4. Conclusão
- Em Python, **todo procedimento é tecnicamente uma função**, pois tudo é tratado como uma função.
- A diferença está no **uso do `return`**:
  - **Se retorna um valor**, é uma **função**.
  - **Se não retorna ou retorna `None`**, é um **procedimento**.
- Essa distinção é mais conceitual em Python, diferente de outras linguagens como Pascal e C, onde procedimentos são declarados de forma separada.

