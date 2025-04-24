import json #importamos la libreria json para trabajar con archivos JSON

def generar_json(direccion_archivo,datos): #Funcion que genera un archivo JSON

    try:
        with open(direccion_archivo,'w') as archivo_json:
            json.dump(datos, archivo_json, indent=4, ensure_ascii=False) #indent es el numero de espacios que se van a usar para dar formato al JSON
            #json.dump es una funcion que convierte un objeto de Python a un archivo JSON
        print("El archivo se ha generado con exito.")
    except Exception as e: #si ocurre un error se captura
        print(f"Ocurrio un error: {e}") #se imprime el error

#El problema que se genera en el json no es de ortografía, sino de codificación de caracteres. Los caracteres especiales como ñ, á, y é 
#están representados en el archivo JSON con su equivalente en Unicode (por ejemplo, \u00f1 para ñ y \u00e1 para á). Esto ocurre porque 
#la función json.dump utiliza por defecto la opción ensure_ascii=True, lo que fuerza a que todos los caracteres no ASCII sean escapados.
#para darle solucion a esto se utiliza ensure_ascii=False, esto permite que los caracteres no ASCII se escriban tal cual en el archivo JSON

#ejemplo de JSON

# Cambiamos el contexto a libros
datos = {
    "titulo": "Cien Años de Soledad", #titulo del libro
    "autor": "Gabriel García Márquez", #autor del libro
    "ano_publicacion": 1967, #ano de publicacion
    "genero": "Realismo Mágico", #genero del libro
    "capitulos": [ 
        {"numero": 1, "titulo": "Capítulo Uno"},
        {"numero": 2, "titulo": "Capítulo Dos"},
        {"numero": 3, "titulo": "Capítulo Tres"}
    ] #lista de capitulos que contiene el libro
}

direccion = r"C:\Users\Santi\Desktop\Parcial\archivos" #direccion del archivo
generar_json(direccion, datos) #se llama a la funcion y se le pasa la direccion y los datos