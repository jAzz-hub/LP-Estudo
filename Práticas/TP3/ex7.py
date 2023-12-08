'''

    Questão 7
    
    Verifique se todos os elementos de uma lista são distintos 
'''

list1 = lambda : [x for x in range(1,6)]+[x for x in range(4,7)]


sorted_list = lambda array: sorted(array)


distinct_search = lambda array, length : False if array[length] == array[length-1] else (distinct_search(array, length-1 if length!=0 else True))

distintos = lambda : distinct_search( sorted_list(list1()), len(list1())-1 )

print(sorted_list(list1()))

print(distintos())
