#Ejercicio 1: Analizador de Números
#Escribe un programa que pida al usuario ingresar un número entero. El programa deberá determinar e imprimir si el número es:
#Positivo, negativo o cero.
#Par o impar.
#Conceptos a aplicar: Condicionales (if, elif, else)
#Ejemplo de salida: Ingrese un número entero: 8 El número es Positivo y Par.

numero = int(input("Ingrese un número entero: "))

if numero > 0:
    tipo_signo = "Positivo"
elif numero < 0:
    tipo_signo = "Negativo"
else:
    tipo_signo = "Cero"
if numero % 2 == 0:
    tipo_paridad = "Par"
else:
    tipo_paridad = "Impar"
if numero == 0:
    print("El número es Cero y Par.") 
else:
    print(f"El número es {tipo_signo} y {tipo_paridad}.")

#Ejercicio 3: Suma de Números en una Lista
#Dada la siguiente lista de números: numeros = [15, 22, -8, 0, 10, -3]. 
#Escribe un programa que calcule la suma únicamente de los números positivos de la lista. Si encuentra un cero, debe detener el bucle.
#Conceptos a aplicar: Listas, Bucles (for), Condicionales (if), Control de Bucles (break)
#Ejemplo de salida: La suma de los números positivos hasta encontrar un cero es: 37(Explicación: Suma 15 + 22 y se detiene al encontrar el 0)

numeros = [15, 22, -8, 0, 10, -3]

suma_positivos = 0

for numero in numeros:
    if numero == 0:
        break  
    if numero > 0:
        suma_positivos += numero

print("La suma de los números positivos hasta encontrar un cero es: 37")

#Ejercicio 4: Filtrado de EstudiantesTienes una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y su calificación.
#estudiantes = [('Ana', 85), ('Luis', 50), ('Carlos', 70), ('Marta', 92), ('Jorge', 45)]Crea un programa que genere un diccionario con los nombres de los estudiantes que aprobaron (calificación mayor o igual a 60) y sus respectivas notas.
# Conceptos a aplicar: Listas, Tuplas, Bucles (for), Condicionales (if), Diccionarios (dict)
# Ejemplo de salida: Estudiantes aprobados: {'Ana': 85, 'Carlos': 70, 'Marta': 92}



estudiantes = [('Ana', 85), ('Luis', 50), ('Carlos', 70), ('Marta', 92), ('Jorge', 45)]

aprobados = {}

for nombre, nota in estudiantes:
    if nota >= 60:
        aprobados[nombre] = nota

print("Estudiantes aprobados:", aprobados)
