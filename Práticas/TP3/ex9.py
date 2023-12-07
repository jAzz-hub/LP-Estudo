'''

    Questão 9
    
    Verificar se uma lista de interios é palíndromo

'''
list1 = lambda : [x for x in range(1,6)]+[x for x in range(6,0,-1)]

palindromo = lambda array : verifyEvenLength(array, 0, len(array)-1) if len(array) % 2 == 0 else verifyOddLength(array, 0, len(array)-1)

#[1,2,3,4,3,2,1]
verifyOddLength = lambda array, first, last:  verifyOddLength(array, first+1, last-1) if array[first] == array[last] and first != round(len(array)/2)  else( True if array[first] == array[last] else False)


#[1,2,3,3,2,1]
verifyEvenLength = lambda array, first, last:  verifyEvenLength(array, first+1, last-1) if array[first] == array[last] and first != round(len(array)/2)  else( True if array[first] == array[last] else False)

print(palindromo(list1()))
