"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    total = 0
    # Ruta corregida según la estructura de carpetas
    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split("\t")
            total += int(partes[1])
    return total


print(pregunta_01())
    