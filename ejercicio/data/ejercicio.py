# proceso 
#
# acceder al archivo
archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# obtener las líneas del archivo
lineas = archivo.readlines()

for i, linea in enumerate(lineas):
    if i == 0:
        encabezados = linea.strip().split("|")
        print("Encabezados:")
        print(encabezados)
    else:
        linea = linea.strip().split("|")
        print(f"Linea {i}: {linea}")
        archivo_generado = open("%s.html" % linea[0], "w")
archivo_generado.writelines("%s" % pagina)
archivo_generado.close()

archivo.close()

pagina = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
  <b>%s:</b> %s  
  </body>
</html>
""" % (encabezados[1], linea[1])

print(pagina)
