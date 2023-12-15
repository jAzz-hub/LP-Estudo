def soma_impares(lista):
    if not lista:  # Se a lista estiver vazia, retorna 0
        return 0
    elif lista[0] % 2 != 0:  # Se o primeiro elemento for ímpar, adiciona-o ao somatório
        return lista[0] + soma_impares(lista[1:])
    else:
        return soma_impares(lista[1:])  # Se o primeiro elemento não for ímpar, continua a recursão com o restante da lista

# Exemplo de uso:
lista_exemplo = [1, 3, 2, 7, 4, 6, 5]
resultado = soma_impares(lista_exemplo)
print(resultado)