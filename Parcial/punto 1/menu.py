from libros_modularizado import GeneradorJSON
from libros_modularizado import Biblioteca

def menu():
    direccion_archivo = r"C:\Users\Santi\Desktop\Parcial\archivos\biblioteca\libros.json"  # Cambia la ruta si es necesario
    generador_json = GeneradorJSON(direccion_archivo)
    biblioteca = Biblioteca(generador_json)

    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamar al menú
if __name__ == "__main__":
    menu()