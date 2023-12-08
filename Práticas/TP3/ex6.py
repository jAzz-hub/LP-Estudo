'''

    Questão 6
    
    Verifique se um número é igual a soma de seus divisores (exceto o próprio número)
     
'''

from random import randint

numero = lambda : randint(0, 100)

divisores = lambda number : [i for i in range(1,number) if number % i == 0] 

perfect_number = lambda number, divisors : True if number == sum(divisors) else False

list_of_divisors = lambda array: [f'{i} + ' for i in array]

output = lambda num : f'Perfeito {num} -- {num} = { str(list_of_divisors(divisores(num))).replace(",", "").replace("[","").replace("]","") } 'if perfect_number(num, divisores(num)) else f'Não perfeito {num} -- {num} ≠ { str(list_of_divisors(divisores(num))).replace(",", "").replace("[","").replace("]","") } '

print(output(numero()).replace("'",'')[:-3])