from tienda import SistemaTienda, Electronico, Ropa, Alimento
from datetime import datetime

# Menú interactivo
def menu():
    tienda = SistemaTienda()

    while True:
        print("\n--- Menú de la Tienda ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Realizar pedido")
        print("4. Guardar productos en archivo JSON")
        print("5. Cargar productos desde archivo JSON")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar Producto ---")
            tipo = input("Ingrese el tipo de producto (Electronico, Ropa, Alimento): ").capitalize()
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad disponible: "))

            if tipo == "Electronico":
                garantia = input("Garantía (en meses): ")
                producto = Electronico(nombre, precio, cantidad, garantia)
            elif tipo == "Ropa":
                tamaño = input("Talla: ")
                producto = Ropa(nombre, precio, cantidad, tamaño)
            elif tipo == "Alimento":
                fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")
                try:
                    datetime.strptime(fecha_caducidad, "%Y-%m-%d")
                except ValueError:
                    print("Fecha inválida. Intente nuevamente.")
                    continue
                producto = Alimento(nombre, precio, cantidad, fecha_caducidad)
            else:
                print("Tipo de producto no válido.")
                continue

            tienda.agregar_producto(producto)
            print("Producto agregado exitosamente.")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            tienda.mostrar_productos()

        elif opcion == "3":
            print("\n--- Realizar Pedido ---")
            nombre_producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a comprar: "))
            tienda.realizar_pedido(nombre_producto, cantidad)

        elif opcion == "4":
            print("\n--- Guardar Productos en JSON ---")
            archivo = input("Nombre del archivo (con extensión .json): ")
            tienda.guardar_productos_json(archivo)

        elif opcion == "5":
            print("\n--- Cargar Productos desde JSON ---")
            archivo = input("Nombre del archivo (con extensión .json): ")
            tienda.cargar_productos_json(archivo)

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()