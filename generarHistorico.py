from datetime import date, timedelta
import random
numContenedores = 10
hoy = date(day=25, month=10, year=2019)
primerDia = date(day=1, month=1, year=2017)  # 1028 datos
capacidad = 100
separador = "#"

for i in range(1, numContenedores + 1):
    diaActual = primerDia
    kgTotal = 0
    # Crear fichero
    nomFich = "Contenedor_" + str(i)
    f = open(nomFich, "w")
    while hoy > diaActual:
        # Generar datos

        # Fecha
        f.write(str(diaActual.day) + "/" + str(diaActual.month) + "/" + str(diaActual.year))
        f.write(separador)

        # Dia de la semana
        f.write(str(diaActual.isoweekday()))
        f.write(separador)

        # Kg hoy (L-V 20-40 | S-D 30-50)
        kgHoy = round((random.randint(20, 40) + random.random() if (diaActual.isoweekday() <= 5) else random.randint(30, 50) + random.random()), 2)
        f.write(str(kgHoy))
        f.write(separador)

        # Kg totales
        kgTotal += round(((kgTotal + kgHoy) % capacidad), 2)
        if kgTotal > 100:
            kgTotal -= 100
        f.write(str(kgTotal))
        f.write(separador)

        # Porcentaje
        porcentaje = round(kgTotal/capacidad * 100, 2)
        f.write(str(porcentaje) + "%")

        diaActual += timedelta(days=1)
        f.write("\n")
    f.close()


