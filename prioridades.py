def prioridad(contenedor):
    # Abrir fichero y leer datos
    fichero = contenedor.getFichero()
    porcentajeOcupado = contenedor.getPorcentaje()
    f = open(fichero)
    datos = []
    for linea in f:
        datos.append(linea)

    prio = porcentajeOcupado
    kgDisponibles = contenedor.getDisponible()
    mediaKg = datos[len(datos) - 7].split("#")[2]
    numSemanas = 1
    for i in range(len(datos) - 14, 0, -7):
        antiguedad = len(datos) - i
        kgDiasAnteriores = int(datos[i].split("#")[2])
        mediaKg = (mediaKg + (kgDiasAnteriores / antiguedad)) / numSemanas
        numSemanas += 1
    return prio + mediaKg - kgDisponibles



