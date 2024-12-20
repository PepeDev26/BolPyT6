def contar_palabra_en_fichero(nombre_fichero, palabra):
    contador = 0
    with open(nombre_fichero, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            contador += linea.lower().split().count(palabra.lower())
    return contador

# Ejemplo de uso
numero_apariciones = contar_palabra_en_fichero('FicheroEjercicio1.txt', 'deckard')
print(numero_apariciones)