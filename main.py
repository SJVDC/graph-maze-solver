"""
main.py
"""

import os
import sys

from src.core.converter import matriz_a_grafo
from src.evaluations.metrics import evaluar_todos
from src.io.maze_reader import process_maze


def main():
    print("=== PROJECT: MAZE SOLVER (GRAPH SEARCH) ===")

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the maze file path (.txt): ").strip()

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' was not found.")
        return

    matrix, rows, cols, start, goal = process_maze(file_path)
    print(f"\nMaze loaded ({rows}x{cols}) | Start: {start} | Goal: {goal}")

    graph = matriz_a_grafo(matrix)
    results = evaluar_todos(graph, start, goal)

    print(f"\n{'Algorithm':<12} | {'Status':<10} | {'Steps':<10} | {'Time (ms)':<12}")
    print("-" * 52)
    for name, data in results.items():
        status = "Success" if data["exito"] else "Failed"
        print(f"{name:<12} | {status:<10} | {data['pasos']:<10} | {data['tiempo_ms']:.4f}")
    print("-" * 52)

    print("\n--- FOUND PATHS ---")
    for name, data in results.items():
        if data["exito"]:
            print(f"\n{name} path ({data['pasos']} steps):")
            print(data["camino"])
        else:
            print(f"\n{name}: No path found.")


if __name__ == "__main__":
    main()