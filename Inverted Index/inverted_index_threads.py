import os
import threading
import time  # Importa el módulo time para medir el tiempo

# Directorio que contiene los archivos de texto
directorio = "C:\\Users\\mauri\\Escritorio\\books_txt"

# Diccionario compartido para almacenar el índice invertido
indice_invertido = {}

# Función para procesar un archivo en busca de tokens y construir el índice invertido
def procesar_archivo(archivo_ruta):
    
    # Obtén el nombre del hilo actual
    nombre_hilo = threading.current_thread().name
    print(f"Hilo {nombre_hilo} procesando archivo: {archivo_ruta}")
    
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

# Lista para almacenar los hilos
hilos = []

# Límite de hilos
limite_hilos = 8

# Inicia la medición del tiempo al comienzo del proceso
tiempo_inicio =  time.time()

# Recorre los archivos en el directorio
for archivo_nombre in os.listdir(directorio):
    if archivo_nombre.endswith(".txt"):
        archivo_ruta = os.path.join(directorio, archivo_nombre)
        # Verifica si hemos alcanzado el límite de hilos
        if len(hilos) >= limite_hilos:
            # Espera a que al menos un hilo termine antes de crear uno nuevo
            hilos[0].join()
            del hilos[0]
        # Crea un hilo para procesar el archivo y agrégalo a la lista de hilos
        hilo = threading.Thread(target=procesar_archivo, args=(archivo_ruta,))
        hilos.append(hilo)
        hilo.start()

# Espera a que todos los hilos restantes terminen
for hilo in hilos:
    hilo.join()

# Finaliza la medición del tiempo al final del proceso
tiempo_fin = time.time()

# Calcula el tiempo total transcurrido
tiempo_total = tiempo_fin - tiempo_inicio

# Imprime el índice invertido
for palabra, documentos in indice_invertido.items():
    print(f"{palabra}: {documentos}")

# Imprime el tiempo total transcurrido
print(f"Tiempo total transcurrido: {tiempo_total} segundos")