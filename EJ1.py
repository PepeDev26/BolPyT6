import unicodedata

def eliminar_tildes(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        texto = f.read()

    texto_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(texto_sin_tildes)

# Ejemplo de uso
eliminar_tildes('FicheroEjercicio1.txt', 'FicheroEjercicio1_sin_tildes.txt')