# Graph Maze Solver

This project solves a maze represented as a matrix, converts it into a graph, and then applies search algorithms to find a path from the start to the goal.

## Objective

The program allows you to:

- read a maze file
- identify the starting position and goal position
- convert the matrix into a graph
- traverse the graph using searches such as:
  - depth-first search
  - breadth-first search
  - A*

## Project structure

- `data/maze.txt`: maze file
- `src/io/maze_reader.py`: maze reading and parsing
- `src/core/graph.py`: main graph class
- `src/core/converter.py`: matrix-to-graph conversion
- `src/search/blind_search.py`: blind searches
- `src/search/informed_search.py`: informed search using A*
- `src/heuristic/calculator.py`: Manhattan heuristic calculation
- `test/`: project tests
- `graph.py`: simple graph version for general use

## How to run

From the project root:

```bash
python3 test/test_epic1.py
```

You can also run the other tests:

```bash
python3 test/test_epic2.py
python3 test/test_epic3.py
python3 test/test_epic4.py
python3 test/test_epic5.py
```

## Maze rules

- `0`: empty cell
- `1`: wall
- `2`: start
- `3`: goal

The matrix is converted into graph nodes, and valid movements are up, down, left, and right.

## Note

This project is designed to be simple and easy to follow, with clear logic for each stage of the process.
