"""
tests/test_epica5.py
Prueba de ejecución de la Épica 5 (Evaluación y Comparativa de Desempeño).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.io.LeerLaberinto import procesar_laberinto
from src.core.converter import matriz_a_grafo
from src.evaluations.metrics import evaluar_todos


def probar_epica_5(ruta_txt):
    if not os.path.exists(ruta_txt):
        print(f"Error: El archivo '{ruta_txt}' no fue encontrado.")
        return

    # 1. Cargar matriz y construir grafo
    matriz, filas, cols, inicio, meta = procesar_laberinto(ruta_txt)
    grafo = matriz_a_grafo(matriz)

    # 2. Ejecutar la evaluación comparativa
    resultados = evaluar_todos(grafo, inicio, meta)

    # 3. Mostrar reporte estructurado por consola
    print(f"\n==================================================")
    print(f"       REPORTE DE DESEMPEÑO - ÉPICA 5             ")
    print(f"==================================================")
    print(f"Archivo: {ruta_txt}")
    print(f"Inicio: {inicio} | Meta: {meta}\n")

    print(
        f"{'Algoritmo':<12} | {'Estado':<10} | {'Pasos (Costo)':<15} | {'Tiempo (ms)':<12}"
    )
    print("-" * 58)

    for nombre_alg, datos in resultados.items():
        estado = "Éxito" if datos["exito"] else "Falló"
        pasos = datos["pasos"]
        tiempo = f"{datos['tiempo_ms']:.4f}"
        print(f"{nombre_alg:<12} | {estado:<10} | {pasos:<15} | {tiempo:<12}")

    print("=" * 58)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
    else:
        ruta_archivo = input(
            "Ingrese la ruta del archivo .txt a probar: "
        ).strip()

    probar_epica_5(ruta_archivo)