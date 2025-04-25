import json

class GeneradorJSON:
    def __init__(self, direccion_archivo):
        self.direccion_archivo = direccion_archivo

    def generar(self, datos):
        try:
            with open(self.direccion_archivo, 'w') as archivo_json:
                json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
            print("El archivo se ha generado con éxito.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Crear una instancia de la clase GeneradorJSON
generador = GeneradorJSON(r"C:\Users\Santi\Desktop\Parcial\archivos\biblioteca\libro.json") #el archivo se guarda en la ruta especificada, con el nombre libro.json

# Llamar al método generar con los datos
generador.generar({
    "titulo": "Cien Años de Soledad",
    "autor": "Gabriel García Márquez",
    "ano_publicacion": 1967,
    "genero": "Realismo Mágico",
    "capitulos": [
        {"numero": 1, "titulo": "Capítulo Uno"},
        {"numero": 2, "titulo": "Capítulo Dos"},
        {"numero": 3, "titulo": "Capítulo Tres"}
    ]
})