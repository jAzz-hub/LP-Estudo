def substituir(valor_antigo, valor_novo, lista):
    if not lista:  # Se a lista estiver vazia, retorna a lista vazia
        return []
    elif lista[0] == valor_antigo:  # Se o primeiro elemento for igual ao valor antigo, substitui pelo valor novo
        return [valor_novo] + substituir(valor_antigo, valor_novo, lista[1:])
    else:
        return [lista[0]] + substituir(valor_antigo, valor_novo, lista[1:])  # Se o elemento não for igual, continua a recursão com o restante da lista

# Exemplo de uso:
lista_exemplo = [1, 2, 1, 3, 1]
resultado = substituir(1, 0, lista_exemplo)
print(resultado)