
'''

    Questão 11
    
    Linearizar uma lista de inteiros
    
    input:  [[0,2],[1],[4,3]]

    output: [0,2,1,4,3]
    
'''

from random import randint


random_list = lambda : [randint(x,100) for x in range(randint(5,9),randint(1,5),-2)]

non_linearizing_generator = lambda : [random_list() for i in range(2,6,1)]

returner = lambda num : num

answer = lambda array : [num for listx in array for num in listx]

output = lambda array : print('input: ',array, '\n output:',answer(array))

output(non_linearizing_generator())




