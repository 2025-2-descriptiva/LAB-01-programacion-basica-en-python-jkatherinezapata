"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    conteo = {}

    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split("\t")
            columna_5 = partes[4]
            elementos = columna_5.split(",")

            for elem in elementos:
                clave = elem.split(":")[0]
                conteo[clave] = conteo.get(clave, 0) + 1

    return dict(sorted(conteo.items()))


print(pregunta_09())
