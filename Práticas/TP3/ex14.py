
'''

    Questão 14
    
    obter lista ordenada resultante da intercalação entre duas listas
    
'''

from random import choices
from random import randint

random_list = lambda :  choices(range(1, 100),k=randint(1,6))

answer = lambda array1, array2 : sorted(array1+array2)

output = lambda array1, array2 : print(f'input: \n\t\t vetor 1: {array1} \n\t\t vetor 2: {array2} \n output: \t\t{answer(array1,array2)}')

output(random_list(),random_list())

