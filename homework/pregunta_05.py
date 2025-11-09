"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores = {}
    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "data.csv")

    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])

            if letra not in valores:
                valores[letra] = [valor, valor]
            else:
                if valor > valores[letra][0]:
                    valores[letra][0] = valor
                if valor < valores[letra][1]:
                    valores[letra][1] = valor

    resultado = sorted([(letra, valores[letra][0], valores[letra][1]) for letra in valores])

    return resultado


print(pregunta_05())