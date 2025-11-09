"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_por_letra = {}

    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor


    resultado = sorted(suma_por_letra.items())

    return resultado


print(pregunta_03())