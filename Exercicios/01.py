"""
Variables & Data Types
"""

# 1. Criação de variáveis
mensagem = "Olá, mundo!"         # string
numero_inteiro = 10              # integer
numero_decimal = 3.14            # float
valor_booleano = True            # boolean

# 2. Operações
soma = numero_inteiro + 5  # Adicionando 5 ao integer
nova_mensagem = mensagem + " Boa noite!"  # Concatenando com outra string
comparacao = numero_decimal > 3.0  # Comparando com 3.0
verificacao_booleano = valor_booleano == False  # Verificando se é igual a False

# 3. Funções
tipo_mensagem = type(mensagem)  # Verifica o tipo da variável string
numero_em_string = str(numero_inteiro)  # Converte integer em string

# Para as conversões a seguir, usamos strings contendo números:
string_numerica = "42"
convertido_para_inteiro = int(string_numerica)  # Converte string para integer
convertido_para_float = float(string_numerica)  # Converte string para float

# Exibindo os resultados
print("Soma:", soma)
print("Nova mensagem:", nova_mensagem)
print("Comparação (3.14 > 3.0):", comparacao)
print("Valor booleano é False?", verificacao_booleano)
print("Tipo da variável 'mensagem':", tipo_mensagem)
print("Número como string:", numero_em_string)
print("String convertida para inteiro:", convertido_para_inteiro)
print("String convertida para float:", convertido_para_float)
