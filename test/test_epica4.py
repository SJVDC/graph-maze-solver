"""
tests/test_epica4.py
Prueba de ejecución de la Épica 4 (Heurística y A*).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.io.LeerLaberinto import procesar_laberinto
from src.core.converter import matriz_a_grafo
from src.heuristica.calculator import generador_tabla_heuristica
from src.search.busqueda_informada import busqueda_a_estrella


def probar_epica_4(ruta_txt):
    if not os.path.exists(ruta_txt):
        print(f"Error: El archivo '{ruta_txt}' no fue encontrado.")
        return

    # 1. Cargar matriz (Épica 1)
    matriz, filas, cols, inicio, meta = procesar_laberinto(ruta_txt)

    # 2. Convertir a grafo (Épica 2)
    grafo = matriz_a_grafo(matriz)

    # 3. Calcular heurística h(n)
    tabla_h = generador_tabla_heuristica(grafo, meta)

    # 4. Ejecuación A*
    ruta_a_estrella = busqueda_a_estrella(grafo, inicio, meta)

    print(f"\n--- Prueba Épica 4: {ruta_txt} ---")
    print(f"Punto Inicio: {inicio} -> Punto Meta: {meta}")
    print(f"Valor h(n) en el punto de inicio: {tabla_h[inicio]}")

    if ruta_a_estrella:
        print(f"Ruta A* encontrada (Pasos / Costo Total: {len(ruta_a_estrella) - 1}):")
        print(ruta_a_estrella)
    else:
        print("A* no encontró un camino hacia la meta.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
    else:
        ruta_archivo = input("Ingrese la ruta del archivo .txt a probar: ").strip()

    probar_epica_4(ruta_archivo)