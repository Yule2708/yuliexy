#ejemplo 1
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Yuliexy")

#ejemplo 2

def mult(a, b):
    return a * b

resultado = mult(4, 5)
print("El resultado es:", resultado)

#ejemplo 3 

def calc(radio):
    import math
    return math.pi * (radio ** 2)
radio = 5
area = calc(radio)
print("El area del circulo es: ", round(area, 2))