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

    for i in range(len(datos), 0, -1):
        antiguedad = len(datos) - i
        