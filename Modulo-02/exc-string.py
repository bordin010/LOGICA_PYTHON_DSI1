# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX1
# Crie uma variável chamada texto1 com o valor "Logica"
# usando aspas duplas e exiba o conteúdo.

texto1 = "Logica"
print(texto1)

# EX2
# Crie uma variável chamada texto2 com o valor
# 'Eu sou top em python' usando aspas simples e exiba.

texto2 = 'Eu sou top em python'
print(texto2)

# EX3
# Crie uma string usando aspas simples que contenha
# aspas duplas dentro do texto: copa "padrão fifa".

st = 'Copa "padrão fifa"'
print(st)

# EX4
# Crie uma string usando aspas duplas que contenha
# aspas simples dentro do texto: copa 'padrão fifa'.

st1 = "Copa 'padrão fida'"
print(st1)

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX5
# Crie uma string multilinha representando um menu
# com as opções:
# -A  Exibe ajuda
# -E  Execute agora, quero jogar!

menu = """\
Uso: programa [OPÇÕES]
-A Exibe ajuda
-E Execute agora, quero jogar!
"""

# EX6
# Crie uma string multilinha contendo um poema
# com três versos.

menu2 = """\
Jesus é minha força e nele descansarei
em meio as dificuldades
nele confiarei.
"""

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX7
# Use concatenação automática de literais para unir
# as palavras "Volei" e "top!".

texto = ("Voltei " "Top")
print(texto)

# EX8
# Concatene automaticamente as strings
# "Python", " é ", "demais" em uma única string.

texto3 = ("Python " "É " "Demais.")
print(texto3)

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX9
# Atribua "software" a uma variável chamada st
# e mostre a primeira letra da string.

st2 = "software"
print("Primeira letra:", st2[0])

# EX10
# Usando a mesma string "software",
# mostre a última letra.

print("Última letra:", st2[-1])

# EX11
# Mostre os caracteres do índice 1 até o índice 4
# (sem incluir o 4) da string "software ".

print(st2[1:4])

# EX12
# Mostre os caracteres do início até o índice 3
# da string "software".

print(st2[0:3])

# EX13
# Mostre os caracteres do índice 2 até o final
# da string "software".

print(st2[2:])

# EX14
# Mostre o tamanho da string "software"
# usando a função len().

print("Tamanho:", len(st2))

# EX15
# Acesse o último caractere de "software"
# usando índice positivo (sem usar -1).

print(st2[7])

# EX16
# Mostre os caracteres que estão nos índices pares
# da string "software".

print(st2[::2])

# EX17
# Inverta a string "software".

print(st2[::-1])