#ejemplo 1
diccionario = {
    "Ariangelina Rincon": 15,
    "Brian Mendez": 10,
    "Carlos Villero": 18,
    "Damian Garcia": 13,
    "Deciel Fernandez": 13,
    "Elias Rivas": 18,
    "Fabian Cardenas": 17,
    "Franklin Vecino": 17,
    "Helyanni Rodriguez": 16,
    "Liliana Rincon": 14,
    "Maria Macias": 16,
    "Over Machado": 16,
    "Paul Moran": 14,
    "Ronald Trujilllo": 12,
    "Yuliexy Dimas": 10
}
print("\nLista Original de los Estudiantes y sus Notas.")
for nombre, nota in diccionario.items():
 print(f"\nNombre: {nombre}, Nota: {nota}")  

diccionario["Ariangelina Rincon"]= 21
diccionario["Over Machado"]= 20
diccionario["Brian Mendez"]= 20
diccionario["Carlos Villero"]= 21
diccionario["Damian Garcia"]=21
diccionario["Deciel Fernandez"]= 17
diccionario["Elias Rivas"]= 20
diccionario["Fabian Cardenas"]= 20
diccionario["Franklin Vecino"]= 20
diccionario["Helyanni Rodriguez"]= 21
diccionario["Liliana Rincon"]= 20
diccionario["Maria Macias"]= 24
diccionario["Over Machado"]= 20
diccionario["Paul Moran"]= 20
diccionario["Ronald Trujilllo"]= 20
diccionario["Yuliexy Dimas"]= 21

print("\nLista Modificada de los Estudiantes y sus Edades.")
for nombre, edad in diccionario.items():
 print(f"\nNombre: {nombre}, Edad: {edad}")