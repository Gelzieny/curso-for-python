<h1 align="center">Funções em Python</h1>

### Esses conceitos são fundamentais para entender como funções funcionam em Python e como tornar seu código mais flexível! 🚀

[Exemplo de Parametro e Argumentro](.paramentos_argumentos.md)

----

### Em Python, funções e procedimentos são conceitos que se referem a blocos de código reutilizáveis, mas há uma diferença sutil entre eles:

[Exemplo de Procedimento and Funções](.procedimento%20and%20funcoes.md)

----

### Função Pura vs. Função Não Pura
No contexto da programação funcional, uma **função pura** é aquela que segue duas regras principais:

* **Determinismo**: Para uma mesma entrada, sempre retorna a mesma saída.

* **Sem efeitos colaterais**: Não modifica variáveis externas, não altera o estado do programa, não faz operações de I/O (como escrita em arquivos ou requisições HTTP).

----

### Função Não Pura

Uma **função não pura** viola pelo menos uma das regras acima. Ou seja, ela pode:

* Retornar valores diferentes para os mesmos inputs (depender de variáveis externas).
* Modificar estados globais ou realizar operações de entrada/saída.

[Exemplo de Função pura e Função **Não Pura](.pura_and_inpura.md)

### Função Lambda em Python

Uma **função lambda** é uma **função anônima e curta** que pode ter múltiplos argumentos, mas apenas uma **expressão**.

[Exemplo de Função pura e Função lambda](.fun_lambda.md)

### Subprogramas 
Subprogramas em funções são blocos de código que realizam uma tarefa específica e podem ser chamados dentro de outras funções ou até mesmo dentro do mesmo escopo. No contexto de funções, subprogramas podem ser divididos em:

[Exemplo de Subprogramas em funções](subprograma.md)

### Docstring em Funções

São usadas para documentar o propósito e o comportamento de uma função em Python. Elas são definidas como uma string dentro de três aspas (`"""` ou `'''`) logo após a assinatura da função e servem para descrever o que a função faz, quais são seus parâmetros e o que ela retorna.

[Exemplo de Docstring em funções](subprograma.md)