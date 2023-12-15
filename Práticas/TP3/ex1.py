def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

# Exemplo de uso:
resultado = potencia(2, 3)
print(resultado)