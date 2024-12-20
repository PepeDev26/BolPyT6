import csv

def extraer_columna_csv(nombre_fichero, nombre_variable):
    with open(nombre_fichero, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        columna_datos = [fila[nombre_variable] for fila in lector_csv if nombre_variable in fila]
    return columna_datos

# Ejemplo de uso
datos_columna = extraer_columna_csv('DatosEjercicio2.csv', 'temperatura')
print(datos_columna)