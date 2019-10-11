text = "este es un texto, para ver cuentas palabras se repiten en el texto"
for a in '.\'!")(,;:?':
    text = text.replace(a, ' ')
formacion = text.split(' ')
dictado = {}
for palabra in formacion:
    if len(palabra) == 0:
        continue
    else:
        dictado[palabra.lower()] = dictado.get(palabra.lower(), 0) + 1
print(dictado)
