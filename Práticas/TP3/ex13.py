
'''

    Questão 12
    
    remover os n últimos elementos de uma lista de inteiros
    
'''

from random import choices
from random import randint

random_list = lambda :  choices(range(1, 100),k=randint(1,30))

n = lambda : randint(0,40)

answer = lambda array, n : array[:len(array)-n] if n > 0 and n < len(array) else ([] if len(array)<n else array )

output = lambda array, n : print(f'input: \n\t\t vetor: {array} \n\t\t n = {n} \n\t\t output: {answer(array,n)}')

output(random_list(),n())

