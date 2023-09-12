import os

# Directorio que contiene los archivos de texto
directorio = "C:\\Users\\mauri\\Escritorio\\books_txt"

# Diccionario para almacenar el índice invertido
indice_invertido = {}

# Recorre los archivos en el directorio
for archivo_nombre in os.listdir(directorio):
    if archivo_nombre.endswith(".txt"):
        archivo_ruta = os.path.join(directorio, archivo_nombre)
        with open(archivo_ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            # Tokeniza el contenido (puedes usar expresiones regulares o split)
            tokens = contenido.split()  # Aquí se usa un enfoque simple por espacio en blanco
            # Construye el índice invertido
            for token in tokens:
                token = token.lower()  # Convierte a minúsculas para evitar duplicados
                if token not in indice_invertido:
                    indice_invertido[token] = [archivo_nombre]
                else:
                    if archivo_nombre not in indice_invertido[token]:
                        indice_invertido[token].append(archivo_nombre)

# Imprime el índice invertido
for palabra, documentos in indice_invertido.items():
    print(f"{palabra}: {documentos}")
