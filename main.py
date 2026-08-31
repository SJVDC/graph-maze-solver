"""
main.py
"""

import os
import sys

from src.core.converter import matriz_a_grafo
from src.evaluations.metrics import evaluar_todos
from src.io.LeerLaberinto import procesar_laberinto


def main():
    print("=== PROYECTO: MAZE SOLVER (GRAFOS Y BÚSQUEDA) ===")

    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
    else:
        ruta_archivo = input(
            "Ingrese la ruta del archivo del laberinto (.txt): "
        ).strip()

    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return

    # 1. Cargar matriz y construir Grafo
    matriz, filas, cols, inicio, meta = procesar_laberinto(ruta_archivo)
    print(
        f"\nLaberinto cargado ({filas}x{cols}) | Inicio: {inicio} | Meta: {meta}"
    )

    grafo = matriz_a_grafo(matriz)

    # 2. Evaluar algoritmos
    resultados = evaluar_todos(grafo, inicio, meta)

    # 3. Mostrar Tabla de Desempeño
    print(
        f"\n{'Algoritmo':<12} | {'Estado':<10} | {'Pasos':<10} | {'Tiempo (ms)':<12}"
    )
    print("-" * 52)
    for nombre, datos in resultados.items():
        estado = "Éxito" if datos["exito"] else "Falló"
        print(
            f"{nombre:<12} | {estado:<10} | {datos['pasos']:<10} | {datos['tiempo_ms']:.4f}"
        )
    print("-" * 52)

    # 4. Presentar las Rutas Encontradas
    print("\n--- RUTAS ENCONTRADAS ---")
    for nombre, datos in resultados.items():
        if datos["exito"]:
            print(f"\nRuta {nombre} ({datos['pasos']} pasos):")
            print(datos["camino"])
        else:
            print(f"\n{nombre}: No encontró ruta.")


if __name__ == "__main__":
    main()