#tienda de maquillaje

def mostrar_menu():
    print("Bienvenido a la tienda de maquillaje")
    print("1. Agregar producto al carrito")
    print("2. Ver carrito")
    print("3. Eliminar producto del carrito")
    print("4. Total de la compra")
    print("5. Salir")
    return input("Seleccione una opción (1-5): ")

def agregar_producto(carrito):
    nombre_de_producto= input("Ingrese el nombre del producto: ")
    precio_de_producto= float( input("Ingrese el precio del producto:"))
    cantidad_de_producto= int(input("Ingrese la cantidad del producto: "))


    if nombre_de_producto in carrito:
        carrito[nombre_de_producto]['cantidad_de_producto'] += cantidad_de_producto

    else:

        carrito[nombre_de_producto] = {'precio_de_producto' : precio_de_producto, 'cantidad_de_producto' : cantidad_de_producto}
        print (f"{cantidad_de_producto} {nombre_de_producto}(s) Han sido añadidos al carrito.")

def ver_carrito(carrito):

    if not carrito:
        print("El carrito esta vacio")
        return
    print("Productos en el carrito: ")

    for nombre_de_producto, detalles in carrito.items():
        precio_de_producto = detalles['precio_de_producto']
        cantidad_de_producto = detalles['cantidad_de_producto']
        print(f"{nombre_de_producto}: {cantidad_de_producto} x ${precio_de_producto:.2f} = ${precio_de_producto * cantidad_de_producto:.2f}")

def eliminar_producto(carrito):

    ver_carrito(carrito)
    if not carrito: 
        print("El carrito esta vacio, no se puede eliminar ningun producto")
        return
    nombre_de_producto = input("Ingrese el nombre del producto a eliminar: ")

    if nombre_de_producto in carrito:
        del carrito[nombre_de_producto]
        print(f"{nombre_de_producto} ha sido eliminado del carrito.")
    else: 
        print(f"El producto {nombre_de_producto} no se encuentra en el carrito.")

def total_compra(carrito):

    if not carrito:
        print("El carrito esta vacio, no se puede calcular el total de la compra")
        return
    total = 0

    for detalles in carrito.values():
        precio_de_producto = detalles['precio_de_producto']
        cantidad_de_producto = detalles['cantidad_de_producto']
        total += precio_de_producto * cantidad_de_producto
    print(f"El total de la compra es: ${total:.2f}")
   
def main():
    
    carrito={}
    print("Bienvenido a la tienda de maquillaje")
    
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            agregar_producto(carrito)
        elif opcion == '2':
            ver_carrito(carrito)
        elif opcion == '3':
            eliminar_producto(carrito)
        elif opcion == '4':
            total_compra(carrito)
        elif opcion == '5':
            print("Gracias por visitar la tienda de maquillaje. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()