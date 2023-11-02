def fibonacci(numero):
    resultado = None

    for i in range(numero):
        if i <= 1:
            resultado = 1
        else:
            j=i-1
            k=j-1
            resultado=fibonacci(j)+fibonacci(k)
    return resultado

print(fibonacci(5))