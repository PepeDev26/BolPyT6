import re

def contar_fechas_en_fichero(nombre_fichero):
    patron_fecha = re.compile(r'\b\d{4}\b')
    contador = 0
    with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            contador += len(patron_fecha.findall(linea))
    return contador

# Ejemplo de uso
numero_fechas = contar_fechas_en_fichero('DatosEjercicio4.txt')
print(numero_fechas)