# Embaralha palavra. Construa uma função que receba uma string como parâmetro
#
# e devolva outra string com os carateres embaralhados.
#
# Por exemplo: se função receber a palavra python, pode
#
# retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
#
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
#
# independentemente de como foram digitados.


from lista08.ipc import funcoes
import random

def embaralha(nome):
    a=list(range(0,len(nome)-1))
    random.shuffle(a)
    for i in range(len(a)):
        print(nome[i])
nome=input()
embaralha(nome)
