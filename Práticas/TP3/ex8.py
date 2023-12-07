'''

    Questão 8
    
    Verificar se duas listas são disjuntas

'''

#Enquanto itera o vetor:
	#  Se o valor já está no set return false
	# else set.add(valor) 

from functools import reduce

disjuntas = lambda : all( i not in [range(1,6)] for i in [range(8,4,-1)])

print(disjuntas())
