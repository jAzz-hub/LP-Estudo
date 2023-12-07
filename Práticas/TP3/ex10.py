'''

    Questão 10
    
    Calcular todas as somas parciais de uma lista de inteiros

'''
list1 = lambda : [x for x in range(6,0, -1)]

sum_from_0_to_limit = lambda array, i, r, limit: sum_from_0_to_limit(array, i+1, r+array[i], limit) if i <= limit else r

somas_parciais = lambda array : [sum_from_0_to_limit(array, 0, 0, index) for index in range(0, len(array))]

print(list1())

print(somas_parciais(list1()))
