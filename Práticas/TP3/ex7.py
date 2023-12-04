'''

    Questão 7
    
    Verifique se todos os elementos de uma lista são distintos utilizando estritamente o paradígma funcional

'''

from functools import reduce

output = lambda : all( i not in [range(1,6)] for i in [range(8,4,-1)])

print(output())
