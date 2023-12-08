'''

    Questão 5
    
    Retornar uma lista com representação em biário de um número inteiro
     
'''

from random import randint

numero = lambda : randint(0, 100)

binario = lambda num: [i for i in str(bin(num)).replace('b','')]

output = lambda num : print(f' binário {num} -- {binario(num)}')

output(numero())