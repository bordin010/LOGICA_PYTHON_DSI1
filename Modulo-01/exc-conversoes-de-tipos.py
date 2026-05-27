# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá
# daqui a 5 anos.

idade = "25"
print(type(idade))

idade2 = int(idade)
print("Tipo:", type(idade2))

print("Daqui 5 anos, o usuário terá:", idade2 + 5)
print("\n\n")

# EX2
# Converta o número de ponto flutuante 7.999
# para inteiro e observe o resultado.

pontoflutuante = "7.999"
print(type(pontoflutuante))

pontoflutuante2 = int(float(pontoflutuante))
print("Tipo:", type(pontoflutuante2))
print("\n\n")

# EX3
# Converta a string "-3.14" para float
# e multiplique o resultado por 2.

valor = "-3.14"
print(type(valor))

valor2 = float(valor)
print("Tipo:", type(valor2))
print(valor2 * 2)
print("\n\n")

# EX4
# Tente converter a string "cento e vinte"
# para inteiro e observe o que acontece.
# RESPOSTA: 
# frase = "cento e vinte"
# print(type(frase))
# frase2 = int("cento e vinte")
# print("Tipo:", type(frase2))
# DÁ ERRO. Não é possível transformar um string em escrita para um inteiro

# EX5
# Converta o número 42 para string
# e concatene com a palavra " respostas".

numero = 42
numero_str = str(numero)
print("Exc5:", numero_str + " respostas")
print("\n\n")

# EX6
# Use a função complex() para criar
# um número complexo com parte real 3
# e parte imaginária 5.

numero_complexo = complex(3, 5)
print("Valor:", numero_complexo)
print("Tipo:", type(numero_complexo))
print("\n\n")

# EX7
# Converta o número 0 para booleano
# e mostre o resultado.

numero = 0
booleano = bool(numero)
print(booleano)
print("\n\n")

# EX8
# Converta o número -100 para booleano
# e mostre o resultado.

numero = -100
boooleano = bool(numero)
print(boooleano)
print("\n\n")

# EX9
# Converta o número 3.1415 para inteiro
# e depois para string, tudo em uma única linha.

print(str(int(3.1415)))
print("\n\n")

# EX10
# Some um número inteiro (5) com um float (2.3)
# e verifique qual é o tipo do resultado.

soma = 5 + 2.3
print(soma)
print("Tipo:", type(soma))
