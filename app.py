print("Hello World...")

# Esto es un comentario en Python // Comentarios en JavaScript
# Esto es un comentario en Python /* comentarios en JavaScript */

# Como definimos una variable en JS?
# var myVariable = 235

# En python en cambio es
myVariable = 235
myCadenaTexto = "Esto es una cadena de texto"
mySuperVariable = None

# Definimos una funcion que calcule el area de un rectangulo.
# es el equivalente a escribir function en javaScript
def calcularArea( base, altura ):
    areaTotal = None
    areaTotal = base * altura
    return areaTotal

resultado = calcularArea(10, 35)
print(resultado)

# definimos una funcion que cuente hasta el numero pedido
def conteo(hastaNumero):
    # Deberia usar un array [0,1..... hastaNumero]
    #for number in hastaNumero:

    # Construye el array [0,1,.... hastaNumero]
    for number in range(hastaNumero):
        print(number)

conteo(50)

def fibonacci(numero):
    resultado = None

    if numero == 0:
        resultado = 1
    elif numero == 1:
        resultado = 1
    else:
        "Algo mas... para completar..."

    return resultado