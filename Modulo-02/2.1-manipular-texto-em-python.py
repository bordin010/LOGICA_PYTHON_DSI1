# AULA COMPLETA - STRINGS EM PYTHON

# - CRIAÇÃO DE STRINGS
# - STRINGS MULTILINHA
# - ÍNDICES E SLIICES
# - OPERAÇÕES COM STRINGS
# - IMUTABILIDADE
# - MÉTODOS ÚTEIS
# - FORMATAÇÃO DE TEXTO
# - UNICODE E BYTES

# ---------------------------
# 1) CRIAÇÃO DE STRINGS
# ---------------------------
# STRINGS SÃO TEXTOS EM PYTHON.
# PODEM SER CRIADAS USANDO ASPAS SIMPLES OU DUPLAS.

texto1 = "Python"
texto2 = 'Curso de Python'
texto3 = "Copa 'padrão fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1, texto2, texto3, texto4)

# PYHTON PERMITE MISTURAR ASPAS SIMPLES E DUPLAS, DENTRO DS STRINGS SEM PRECISAR ESCAPAR CARACTERES

# ---------------------------------------------
# 2) STRINGS MULTILINHA
# ---------------------------------------------
# USANDO TRÊS ASPAS  (""" OU ''') PARA CRIAR TEXTOS QUE OUPAM VÁRIAS LINHAS.

menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print(menu)

# ESSE FORMATO É MUITO USADO PARA:
# - MENUS
# - DOCUMENTAÇÃO
# - TEXTOS LONGOS

# ---------------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
# ---------------------------------------------
# QUANDO DUAS STRINGS APARECEM LADO A LADO, O PYHTON JUNTA AUTOMATICAMENTE

texto = ("Copa " "2026 " "Neymar é show mesmo? " "Talvez")
print(texto)

# ---------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
# ---------------------------------------------
# UMA STRING FUNÇÃO COMO UMA SEQUÊNCIA DE CARACTERES, CADA CARACTERE POSSUI UM ÍNDICE.

st = "maracana"
print("Primeira letra:", st[0])
# SÓ EXIBIR A LETRA: M

print("Ultima letra:", st[7])

print("Trecho 1:4", st[1:4])

print("Do início até 3:", st[:3])

print ("Do 2 até o fim:", st[2:])

print("Tamanho", len(st))


# ---------------------------------------------
# 5) OPERAÇÕES COM STRINGS
# ---------------------------------------------
# PYTHON PERMITE VÁRIAS OPERAÇÕES COM STRINGS


print("m" in st)
# SIGNIFICA QUE "X" NÃO EXISTE NA STRING

print("m" * 20)
# MULTIPLICAÇÃO REPETE A STRING

print("m" + "aracana")
# OPERADOR + CONCATENA STRINGS


# ---------------------------------------------
# 6) STRINGS SÃO IMUTÁVEIS
# ---------------------------------------------
# STRINGS NÃO PODEM SER ALTERADAS DIRETAMENTE!!!
# ISSO SIGNIFICA QUE O CONTEÚDO ORIGINAL NÃO MUDA.
# O QUE ACONTECE É A CRIAÇÃO DE UMA NOVA STRING.

texto ="python 9"

# MÉTODO REPLACE CRIA UMA NOVA STRING
texto = texto.replace("9", "0")

print(texto)

# ---------------------------------------------
# 7) MÉTODOS IMPORTANTES
# ---------------------------------------------
# STRINGS POSSUEM VÁRIOS MÉTODOS.

cidade = "maracana"
# COLOCA A PRIMEIRA LETRA EM MAIUSCULA.
print(cidade.capitalize())

# CONTA QUANTAS VEZES "A" APARECE
print(cidade.count("a"))

# VERIFICAR SE COMEÇA COM "M"
print(cidade.startswith("m"))

# VERICA SE TERMINA COM "Z"
print(cidade.endswith("z"))

frase = "copa de 2002"

# DIVIDE A STRING EM UMA LISTA
print(frase.split(" "))

# ---------------------------------------------
# 8) FORMATAÇÃO DE STRINGS
# ---------------------------------------------