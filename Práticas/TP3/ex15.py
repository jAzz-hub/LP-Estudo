
'''

    Questão 15
    
    obter lista ordenada resultante da intercalação entre duas listas
    
'''

from random import choices
from random import randint
from math import floor

valor = lambda :  randint(0,400)


fx = lambda value : list(map ( lambda valor_das_notas : fx(valor - (value % valor_das_notas)), [100,50,10,5,1]))

# for i in fx(valor()):
print(fx)
a = []
# notas = [100,50,10,5,1],
# fg = lambda value, i, array : fg(value % [100,50,10,5,1][i],[100,50,10,5,1],i+1,array+[floor(valor / [100,50,10,5,1][i])]) if value % [100,50,10,5,1][i] != 0 else array

# print(fg(320,0,a))

# output = lambda valor: print(f'input: \n\t\t valor: {valor} \n\t\t quantas notas: {fx(valor)} \n output: \t\t{234}')

# output(valor())

