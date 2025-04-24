import json
from datetime import datetime
import os

# Clase base Producto
class Producto:
    """Clase base para productos"""
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_stock(self, cantidad_comprada):
        if cantidad_comprada <= self.cantidad:
            self.cantidad -= cantidad_comprada
            return True
        return False

    def calcular_precio_total(self, cantidad_comprada):
        total = self.precio * cantidad_comprada
        if cantidad_comprada > 5:
            total *= 0.9  # 10% de descuento
        return total

# Subclases
class Electronico(Producto):
    """Producto electrónico con garantía"""
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

class Ropa(Producto):
    """Producto de ropa con tamaño"""
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.tamaño = tamaño

class Alimento(Producto):
    """Producto alimenticio con fecha de caducidad"""
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad

# Sistema de gestión
class SistemaTienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra los productos con sus atributos específicos"""
        for producto in self.productos:
            info = f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}"
            if isinstance(producto, Electronico):
                info += f", Garantía: {producto.garantia} meses"
            elif isinstance(producto, Ropa):
                info += f", Tamaño: {producto.tamaño}"
            elif isinstance(producto, Alimento):
                info += f", Fecha de caducidad: {producto.fecha_caducidad}"
            print(info)

    def realizar_pedido(self, nombre_producto, cantidad):
        """Realiza un pedido si hay stock suficiente"""
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad < cantidad:
                    print(f"Stock insuficiente. Solo hay {producto.cantidad} unidades disponibles.")
                    return
                if producto.actualizar_stock(cantidad):
                    total = producto.calcular_precio_total(cantidad)
                    print(f"Pedido realizado. Total a pagar: ${total:.2f}")
                    return
        print("Producto no encontrado.")

    def guardar_productos_json(self, archivo):
            """Guarda los productos en un archivo JSON dentro de la carpeta 'archivos/tienda'"""
            try:
                carpeta = "archivos/tienda"
                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)  # Crea la carpeta si no existe

                ruta_completa = os.path.join(carpeta, archivo)

                productos_serializables = []
                for producto in self.productos:
                    producto_dict = {
                        "tipo": producto.__class__.__name__,
                        "nombre": producto.nombre,
                        "precio": producto.precio,
                        "cantidad": producto.cantidad
                    }
                    if isinstance(producto, Electronico):
                        producto_dict["garantia"] = producto.garantia
                    elif isinstance(producto, Ropa):
                        producto_dict["tamaño"] = producto.tamaño
                    elif isinstance(producto, Alimento):
                        producto_dict["fecha_caducidad"] = producto.fecha_caducidad
                    productos_serializables.append(producto_dict)

                with open(ruta_completa, 'w', encoding='utf-8') as file:
                    json.dump(productos_serializables, file, indent=4, ensure_ascii=False)

                print(f"Productos guardados en {ruta_completa}")
            except Exception as e:
                print(f"Error al guardar productos: {e}")

    def cargar_productos_json(self, archivo):
        """Carga productos desde un archivo JSON dentro de la carpeta 'archivos/tienda'"""
        try:
            carpeta = "archivos/tienda"
            ruta_completa = os.path.join(carpeta, archivo)

            with open(ruta_completa, 'r', encoding='utf-8') as file:
                productos_serializables = json.load(file)
                for producto_dict in productos_serializables:
                    tipo = producto_dict.pop("tipo")
                    if tipo == "Electronico":
                        producto = Electronico(**producto_dict)
                    elif tipo == "Ropa":
                        producto = Ropa(**producto_dict)
                    elif tipo == "Alimento":
                        producto = Alimento(**producto_dict)
                    self.agregar_producto(producto)

            print(f"Productos cargados desde {ruta_completa}")
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no fue encontrado en '{carpeta}'.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
        except Exception as e:
            print(f"Ocurrió un error al cargar productos: {e}")
