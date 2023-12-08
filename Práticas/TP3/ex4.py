'''

    Questão 5
    
    Verificar se um número é primo
    
    Referencial para resposta: 
    teste de primalidade por otimização 6k ± 1
    https://en.wikipedia.org/wiki/Primality_test#Python
     
'''

from random import randint
from math import isqrt

numero = lambda : randint(0, 100)

par = lambda num : True if num % 2 == 0 else False

multiplo_de_tres = lambda num : True if num % 3 == 0 else False

menor_que_tres = lambda num :  True if num < 3 and num > 1 else False

teste_1 = lambda num : par(num) or multiplo_de_tres(num)

lista_aux_para_teste = lambda num : [i for i in range(5, isqrt(num)+1, 6)]

teste_2 = lambda num : any([ num % i == 0 or num % (i+2) == 0 for i in lista_aux_para_teste(num)])

primo = lambda num: True if menor_que_tres(num) else(False if teste_1(num) else (False if teste_2(num) else True ))

output = lambda num : print(f'Primo {num} -- {True}' if primo(num) else f'Não primo {num} -- {False}')

output(numero())