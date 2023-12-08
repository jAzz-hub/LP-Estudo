'''

    Questão 10
    
    Calcular todas as somas parciais de uma lista de inteiros

'''
list1 = lambda : [x for x in range(1,5)]

soma_de_zero_ate_x = lambda array, i, r, limit: soma_de_zero_ate_x(array, i+1, r+array[i], limit) if i <= limit else r

somas_parciais = lambda array : [soma_de_zero_ate_x(array, 0, 0, index) for index in range(0, len(array))]

print(list1())

print(somas_parciais(list1()))
