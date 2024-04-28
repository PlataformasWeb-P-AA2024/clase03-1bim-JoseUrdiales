# proceso 
#
# acceder al archivo con codificación UTF-8
archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r", encoding="utf-8")

# obtener las líneas del archivo
lineas = archivo.readlines()

# lineas es una lista de cadenas
# obtengo los encabezados de la primera línea
encabezados = lineas[0]
encabezados = encabezados.strip().split("|")

# Recorro las líneas del archivo a partir de la segunda línea
for linea in lineas[1:]:
    # Limpio la línea de espacios en blanco y la separo por '|'
    linea = linea.strip().split("|")

    # Creo el contenido HTML dinámico con los datos de la línea actual
    contenido_html = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>INFORMACIÓN DE LA INSTITUCIÓN.</title>
      </head>
      <body>
      <h1>INFORMACIÓN DE LA INSTITUCIÓN</h1>
    """
    
    # Agrego las etiquetas <b> y el contenido correspondiente para cada elemento de la línea
    for indice, valor in enumerate(linea):
        # Excluir los índices 10, 11 y 12
        if indice not in [10, 11, 12]:
            contenido_html += "<b>%s:</b> %s<br>" % (encabezados[indice], valor)

    contenido_html += """
      </body>
    </html>
    """

    # Creo un archivo HTML con el nombre de la primera columna de la línea actual
    archivo_generado = open("%s.html" % linea[0], "w", encoding="utf-8")
    archivo_generado.write(contenido_html)
    archivo_generado.close()

archivo.close()
