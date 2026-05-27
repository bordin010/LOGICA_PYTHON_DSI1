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