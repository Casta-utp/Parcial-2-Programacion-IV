import json
import os

class HabitacionSimple:

    habitaciones = {} # Diccionario para almacenar habitaciones

    def __init__(self, numero, precio, estado="disponible", tipo="Habitación Simple"):
        self.__numero = numero
        self.__precio = precio
        self.__estado = estado
        self.tipo = tipo # el tipo de habitacion es para tener una mejor comprension

    # Encapsulamiento con métodos
    def get_numero(self): # Devuelve el número de la habitación
        return self.__numero

    def get_precio(self): # Devuelve el precio de la habitación
        return self.__precio 

    def get_estado(self):
        return self.__estado 

    def set_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "reservado"]:
            self.__estado = nuevo_estado # Cambia el estado de la habitación

    def reservar(self):
        if self.__estado == "disponible": # Verifica si la habitación está disponible
            self.__estado = "reservado" # Cambia el estado a reservado
            print(f"{self.tipo} {self.__numero} reservada con éxito.") #imprime el mensaje de éxito
        else:
            print(f"{self.tipo} {self.__numero} no está disponible.")

    def liberar(self):
        if self.__estado == "reservado": # Verifica si la habitación está reservada
            self.__estado = "disponible" # Cambia el estado a disponible
            print(f"{self.tipo} {self.__numero} liberada con éxito.")
        else:
            print(f"{self.tipo} {self.__numero} ya está disponible.")

    def calcular_precio_total(self):
        return self.__precio # Devuelve el precio total de la habitación

    def __str__(self):
        return f"{self.tipo} {self.__numero} - Precio: ${self.calcular_precio_total()} - Estado: {self.__estado}" # Representación en cadena de la habitación

    def guardar_en_json(self, archivo, habitaciones):
        """
        Guarda las habitaciones en un archivo JSON en una ruta específica predefinida.
        """
        try:
            # Ruta fija de la carpeta donde se guardará el archivo
            carpeta = "archivos/hotel"  # Cambia esta ruta a la que prefieras

            # Combinar la carpeta con el nombre del archivo para obtener la ruta completa
            ruta_completa = os.path.join(carpeta, archivo)

            # Asegurarse de que la ruta del archivo existe
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)  # Crea la carpeta si no existe

            # Convertir las habitaciones a un formato serializable
            habitaciones_dict = {num: {
                'numero': habitacion.get_numero(),
                'precio': habitacion.get_precio(),
                'estado': habitacion.get_estado(),
                'tipo': habitacion.tipo
            } for num, habitacion in habitaciones.items()}
            
            # Escribir en el archivo JSON
            with open(ruta_completa, 'w', encoding='utf-8') as file:
                json.dump(habitaciones_dict, file, ensure_ascii=False, indent=4)
            
            print(f"Habitaciones guardadas exitosamente en el archivo: {ruta_completa}")
        except FileNotFoundError:
            print(f"Error: No se encontró la ruta especificada. Verifica la carpeta.")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en el archivo en la ruta especificada.")
        except Exception as e:
            print(f"Error inesperado al guardar las habitaciones: {e}")



    def cargar_de_json(self, archivo):
            """
            Carga las habitaciones desde un archivo JSON en la carpeta de guardado.
            """
            try:
                # Ruta fija de la carpeta donde se guarda el archivo
                carpeta = "archivos/hotel"  # Cambia esta ruta a la que prefieras

                # Combina la carpeta con el nombre del archivo proporcionado para obtener la ruta completa
                ruta_completa = os.path.join(carpeta, archivo)

                # Verificar si el archivo existe
                if not os.path.exists(ruta_completa):
                    print(f"Error: El archivo {archivo} no se encuentra en la carpeta {carpeta}.")
                    return

                # Cargar las habitaciones desde el archivo JSON
                with open(ruta_completa, 'r', encoding='utf-8') as file:
                    habitaciones_dict = json.load(file)
                    for num, datos in habitaciones_dict.items():
                        # Crear una nueva habitación con los datos cargados
                        habitacion = HabitacionSimple(
                            numero=datos['numero'],
                            precio=datos['precio'],
                            estado=datos['estado'],
                            tipo=datos['tipo']
                        )
                        self.habitaciones[num] = habitacion
                    print(f"Habitaciones cargadas exitosamente desde el archivo: {ruta_completa}")
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo {archivo}. Verifica la ruta.")
            except json.JSONDecodeError:
                print(f"Error: El archivo {archivo} no es un JSON válido.")
            except Exception as e:
                print(f"Error inesperado al cargar las habitaciones: {e}")

class HabitacionDoble(HabitacionSimple):
    def __init__(self, numero, precio, estado="disponible"):
        super().__init__(numero, precio, estado, tipo="Habitación Doble")
        self.servicios_adicionales = []

    def agregar_servicio(self, nombre, precio):
        self.servicios_adicionales.append({"nombre": nombre, "precio": precio})
        print(f"Servicio '{nombre}' (${precio}) agregado a la habitación {self.get_numero()}.")

    def calcular_precio_total(self):
        total_servicios = sum(serv["precio"] for serv in self.servicios_adicionales)
        return self.get_precio() + total_servicios

    def __str__(self):
        if self.servicios_adicionales:
            servicios = ", ".join([f'{s["nombre"]} (${s["precio"]})' for s in self.servicios_adicionales])
        else:
            servicios = "Ninguno"
        return super().__str__() + f" - Servicios adicionales: {servicios}"


class Suite(HabitacionSimple):
    def __init__(self, numero, precio, estado="disponible"):
        super().__init__(numero, precio, estado, tipo="Suite")
        self.servicios_adicionales = []

    def agregar_servicio(self, nombre, precio):
        self.servicios_adicionales.append({"nombre": nombre, "precio": precio})
        print(f"Servicio '{nombre}' (${precio}) agregado a la suite {self.get_numero()}.")

    def calcular_precio_total(self):
        total_servicios = sum(serv["precio"] for serv in self.servicios_adicionales)
        return self.get_precio() + total_servicios

    def __str__(self):
        if self.servicios_adicionales:
            servicios = ", ".join([f'{s["nombre"]} (${s["precio"]})' for s in self.servicios_adicionales])
        else:
            servicios = "Ninguno"
        return super().__str__() + f" - Servicios adicionales: {servicios}"
