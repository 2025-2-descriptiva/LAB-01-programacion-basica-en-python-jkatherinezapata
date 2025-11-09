"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}
    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split("\t")
            letra = partes[0]
            col5 = partes[4].split(",")

            total_fila = 0
            for elem in col5:
                _, valor = elem.split(":")
                total_fila += int(valor)

            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + total_fila

    resultado = dict(sorted(suma_por_letra.items()))

    return resultado


print(pregunta_12())