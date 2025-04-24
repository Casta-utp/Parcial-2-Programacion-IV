from gestion import HabitacionSimple, HabitacionDoble, Suite

def menu_gestion_habitaciones():
    while True:
        print("\n--- Gestión de Habitaciones ---")
        print("1. Agregar habitación")
        print("2. Reservar habitación")
        print("3. Liberar habitación")
        print("4. Mostrar todas las habitaciones")
        print("5. Mostrar habitaciones disponibles")
        print("6. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tipo = input("Tipo (Simple, Doble, Suite): ").strip().lower()
            try:
                numero = int(input("Número de habitación: "))
                if numero in HabitacionSimple.habitaciones:
                    print("Ya existe una habitación con ese número.")
                    continue
                precio = float(input("Precio de la habitación: "))
                if tipo == "simple":
                    habitacion = HabitacionSimple(numero, precio)
                elif tipo == "doble":
                    habitacion = HabitacionDoble(numero, precio)
                elif tipo == "suite":
                    habitacion = Suite(numero, precio)
                else:
                    print("Tipo inválido.")
                    continue
                HabitacionSimple.habitaciones[numero] = habitacion
                print(f"{habitacion.tipo} {habitacion.get_numero()} agregada con éxito.")
            except ValueError:
                print("Datos inválidos.")

        elif opcion == "2":
            try:
                numero = int(input("Número de habitación a reservar: "))
                HabitacionSimple.habitaciones[numero].reservar()
            except:
                print("Número inválido o habitación no encontrada.")

        elif opcion == "3":
            try:
                numero = int(input("Número de habitación a liberar: "))
                HabitacionSimple.habitaciones[numero].liberar()
            except:
                print("Número inválido o habitación no encontrada.")

        elif opcion == "4":
            if HabitacionSimple.habitaciones:
                for hab in HabitacionSimple.habitaciones.values():
                    print(hab)
            else:
                print("No hay habitaciones registradas.")

        elif opcion == "5":
            disponibles = [h for h in HabitacionSimple.habitaciones.values() if h.get_estado() == "disponible"]
            if disponibles:
                for hab in disponibles:
                    print(hab)
            else:
                print("No hay habitaciones disponibles.")

        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def menu_servicios():
    while True:
        print("\n--- Servicios y Precios ---")
        print("1. Agregar servicio a Doble o Suite")
        print("2. Calcular precio total")
        print("3. Mostrar servicios")
        print("4. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                numero = int(input("Número de la habitación: "))
                habitacion = HabitacionSimple.habitaciones.get(numero)
                if isinstance(habitacion, (HabitacionDoble, Suite)):
                    nombre = input("Nombre del servicio: ").strip()
                    precio = float(input("Precio del servicio: "))
                    habitacion.agregar_servicio(nombre, precio)
                else:
                    print("No es una habitación Doble ni Suite.")
            except:
                print("Datos inválidos.")

        elif opcion == "2":
            try:
                numero = int(input("Número de habitación: "))
                habitacion = HabitacionSimple.habitaciones.get(numero)
                if isinstance(habitacion, (HabitacionDoble, Suite)):
                    print(f"Precio total: ${habitacion.calcular_precio_total()}")
                else:
                    print("No es una habitación Doble ni Suite.")
            except:
                print("Número inválido.")

        elif opcion == "3":
            try:
                numero = int(input("Número de habitación: "))
                habitacion = HabitacionSimple.habitaciones.get(numero)
                if isinstance(habitacion, (HabitacionDoble, Suite)):
                    if habitacion.servicios_adicionales:
                        for s in habitacion.servicios_adicionales:
                            print(f"{s['nombre']} - ${s['precio']}")
                    else:
                        print("Sin servicios adicionales.")
                else:
                    print("No es una habitación Doble ni Suite.")
            except:
                print("Número inválido.")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def menu_archivos():
    while True:
        print("\n--- Gestión de Archivos ---")
        print("1. Guardar en archivo JSON")
        print("2. Cargar desde archivo JSON")
        print("3. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            archivo = input("Nombre del archivo (.json): ")
            try:
                HabitacionSimple.guardar_en_json(HabitacionSimple, archivo, HabitacionSimple.habitaciones)
                print("Habitaciones guardadas correctamente.")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            archivo = input("Nombre del archivo (.json): ")
            try:
                HabitacionSimple.cargar_de_json(HabitacionSimple, archivo)
                print("Habitaciones cargadas correctamente.")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# Menú principal
if __name__ == "__main__":
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestión de habitaciones")
        print("2. Servicios y precios")
        print("3. Archivos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_gestion_habitaciones()
        elif opcion == "2":
            menu_servicios()
        elif opcion == "3":
            menu_archivos()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
