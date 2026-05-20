# AULA COMPLETA: NUMERO EM PHYTON
"""
VAMOS APREDER:
1-TIPOS NUMÉRICOS
2-CONVERSÕES DE TIPOS
3-HIERARQUIA NUMÉRICA
4-OPERAÇÕES MATMÁTICAS
4-COERÇÃO DE TIPOS
5-VERIFICÇÃO DE TIPOS
6-ENTRADA DE DADOS
"""

# PASSO 1 - TIPOS NUMÉRICOS #
# INT -> INTEIROS #
# FLOAT -> NÚMERICOS COM CASAS DECIMAIS #
# COMPLEX -> NÚMEROS COMPLEXOS (usado em matematica/engenharia) #

print(" --TIPOS NÚMERICOS-- ")
vendas = 1000

custo = 300
lucro = vendas - custo
print ("o nosso lucro foi de:", lucro, "e a nossas vendas foi de:", vendas)
numeros_interio =10 
#mostrando o valor!!
print("valor:", numeros_interio)

#TYPE () mostra qual é o tipo da variavelag
print("tipo:", type (numeros_interio))

#exemplo 2 - numero decimal
numero_decimal = 3.13
print("tipo:", type(numero_decimal))

#exemplo 3 - numeros cmplexos
#um número complexo possui duas partes:
#numero normal (numero normal)
  #parte imaginária (mutiplicad por j)
#estruturada geral;
#numero =a +bj

# a = parte real
# parte imaginária      
# j = unidade imaginária

numero_complexo = 2+3j
print("valor:", numero_complexo)
print("tipo:", type(numero_complexo))

#git clone e copiar o link

#exemplo 03 - acessando cada parte do número 

# .real retorna a parte real 
print("parte real:", numero_complexo.real)
#.img retorna a parte imaginária 
print ("parte imaginária:", numero_complexo.imag)

# apenas para separar visualmente a saída no terminal
print("\n\n")
  
  #ddaos vindos do usuario são textos (string), muitas vezes é nescessario converter eles

print("=== conversão ====")

# float -> int
valor =int (3.9)
print("int(3.9):", valor)
print("tipo:", type(valor))
 
 #string -> int
valor1 = "10"
print(type, (valor1))

valor2 =int ("10")
print('int ("10"):', valor2)
print("tipo:", type(valor2))

#int --> float
valor3 = float(10)
print("valor(10):", valor3)
print("tipo:", type(valor3))
