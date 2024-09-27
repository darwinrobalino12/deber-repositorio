# 1. Crear el diccionario
informacion_personal = {
    "nombre": "Darwin Robalino",
    "edad": 41,
    "ciudad": "Ambato",
    "profesion": "Mecanico"
}

# 2. Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# 3. Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# 4. Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio

# 5. Eliminar la clave "edad"
informacion_personal.pop("edad", None)  # Usamos pop para eliminar, None previene errores si no existiera

# 6. Imprimir el diccionario resultante
print(informacion_personal)



