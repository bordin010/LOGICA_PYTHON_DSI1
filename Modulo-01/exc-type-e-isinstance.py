# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.

ano = 2024
print("Tipo:", type(ano))
print("\n\n")

# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().

numero = 3.14159
print(isinstance(numero, float))
print("\n\n")

# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.

print(type(100) == type(True))
print("\n\n")

# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.

print(isinstance(True, int))
print("\n\n")

# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().

resultado = 5/2
print("Tipo:", type(resultado))

resultado2 = 5/2
print(isinstance(resultado2, float))
print("\n\n")

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.

def verifica_numero(valor):
    if isinstance(valor, (int, float, complex)):
        print("Ex6: É número")
    else:
        print("Ex6: É número.")

verifica_numero(42)
verifica_numero("texto")
print("\n\n")

# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

valor = True

if type(valor) == int:
    print("type: Booleano é inteiro")
else:
    print("type: Booleano NÃO é inteiro")
    
print("\n\n")

# EX8
# Descubra o tipo do número 3+4j
# usando type().

valor = 3+4j
print("Tipo:", type(valor))
print("\n\n")

# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().

valor = None

if isinstance(valor, type(None)):
    print("O valor é do tipo NoneType")

else:
    print("O valor NÃO é do tipo NoneType")

# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.

numero = 3.0
if isinstance(numero, (int, float, complex)):
    print("É um número")

else:
    print("Não é um número")

if isinstance(numero, int):
    print("É do tipo int")

else:
    print("Não é do tipo int")