import re

def contar_fechas_en_fichero(nombre_fichero):
    patron_fecha = re.compile(r'\b(1[0-9]{3}|2[0-9]{3}|3000|[0-9]{1,3} d\.C\.|[1-9][0-9]{0,3} a\.C\.)\b')
    contador = 0
    with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            contador += len(patron_fecha.findall(linea))
    return contador

# Ejemplo de uso
numero_fechas = contar_fechas_en_fichero('DatosEjercicio5.txt')
print(numero_fechas)