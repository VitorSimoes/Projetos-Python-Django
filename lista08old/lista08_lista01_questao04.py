# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

from lista08old.ipc import funcoes

arg = int(input("Informe o número: "))

resposta = funcoes.positivo_negativo(arg)

print(resposta)