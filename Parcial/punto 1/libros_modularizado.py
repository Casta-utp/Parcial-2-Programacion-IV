import json

class GeneradorJSON:
    def __init__(self, direccion_archivo):
        self.direccion_archivo = direccion_archivo

    def generar(self, datos): #aqui se genera el archivo
        try:
            with open(self.direccion_archivo, 'w') as archivo_json:
                json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
            print("El archivo se ha generado con éxito.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def leer(self): #aqui se lee el archivos
        try:
            with open(self.direccion_archivo, 'r') as archivo_json:
                datos = json.load(archivo_json) #json.load lee el archivo
            print("El archivo se ha leído con éxito.")
            return datos #retorna los datos leidos
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
            return None #retorna None si no se puede leer el archivo


#aqui se crea la clase Biblioteca, que utiliza la clase GeneradorJSON para generar y leer el archivo
class Biblioteca:
    def __init__(self, generador_json):
        self.generador_json = generador_json
        self.libros = self.generador_json.leer() or [] #se inicializa la lista de libros con los datos leidos del archivo, o una lista vacia si no se puede leer el archivo

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        ano_publicacion = int(input("Ingrese el año de publicación: "))
        genero = input("Ingrese el género del libro: ")
        capitulos = [] #se inicializa la lista de capitulos como vacia
        #se pide al usuario que ingrese los capitulos del libro

        while True: #se utiliza un bucle para agregar capitulos
            agregar_capitulo = input("¿Desea agregar un capítulo? (s/n): ").lower() #se convierte la entrada a minusculas, para una mayor comprension
            if agregar_capitulo == 's':
                numero = int(input("Ingrese el número del capítulo: "))
                titulo_capitulo = input("Ingrese el título del capítulo: ")
                capitulos.append({"numero": numero, "titulo": titulo_capitulo})
            else:
                break

        libro = {
            "titulo": titulo,
            "autor": autor,
            "ano_publicacion": ano_publicacion,
            "genero": genero,
            "capitulos": capitulos
        } #se crea un diccionario con los datos del libro
        self.libros.append(libro) #se agrega el libro a la lista de libros
        self.generador_json.generar(self.libros) #se llama al metodo generar de la clase GeneradorJSON para guardar los datos en el archivo
        print("Libro agregado con éxito.")

    def mostrar_libros(self):
        if not self.libros: #si la lista de libros esta vacia
            print("No hay libros en la biblioteca.")
        else:
            for i, libro in enumerate(self.libros, start=1): #se utiliza enumerate para obtener el indice y el libro, el indice comienza en 1
                print(f"\nLibro {i}:")
                print(f"  Título: {libro['titulo']}")
                print(f"  Autor: {libro['autor']}")
                print(f"  Año de publicación: {libro['ano_publicacion']}")
                print(f"  Género: {libro['genero']}")
                print("  Capítulos:")
                for capitulo in libro['capitulos']:
                    print(f"    - Capítulo {capitulo['numero']}: {capitulo['titulo']}")
            #enumerate funciona como un contador

#finalmente, el codigo se encuentra modularizado porque separar la funcionalidad en clases y métodos hace que el 
#código sea más fácil de entender, mantener y reutilizar. 
