
'''

    Questão 12
    
    Realizando shift de 3 índices em uma lista aleatória
    
'''

from random import choices
from random import randint

random_list = lambda :  choices(range(1, 51),k=randint(1,11))

shifter = lambda array : array[3:] + array[:3]

output = lambda array : print('input: ',array,'\n output',shifter(array))

output(random_list())

