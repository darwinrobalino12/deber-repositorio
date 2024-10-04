# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as my_notes:
    # Método write(): escribir líneas de forma individual
    my_notes.write("Línea 1: Esto es una prueba para el deber semana 16.\n")
    my_notes.write("Línea 2: Escribiendo en archivos con Python.\n")

    # Método writelines(): escribir una lista de líneas
    lineas = ["Línea 3: siguiente ejemplo para el deber.\n", "Línea 4: escribimos otro linea para verificar.\n"]
    my_notes.writelines(lineas)

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt para leer su contenido
print('Contenido del archivo my_notes.txt:\n')

# Método 1: read()
with open('my_notes.txt', 'r') as my_notes:
    print('Método 1: read()')
    print('--------------------')
    print(my_notes.read())  # Lee todo el contenido del archivo

# Método 2: readlines()
with open('my_notes.txt', 'r') as my_notes:
    print('Método 2: readlines()')
    print('--------------------')
    for linea in my_notes.readlines():
        print(linea.rstrip('\n'))  # Elimina el salto de línea al final de cada línea