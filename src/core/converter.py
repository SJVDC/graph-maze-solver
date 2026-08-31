from src.core.graph import Graph


def matrix_to_graph(matrix):
    num_rows = len(matrix)
    if num_rows > 0:
        num_cols = len(matrix[0])
    else:
        num_cols = 0

    graph = Graph()
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(num_rows):
        for col in range(num_cols):
            current_value = matrix[row][col]

            if current_value != 1:
                current_node = (row, col)
                graph.add_node(current_node)

                for row_offset, col_offset in movements:
                    new_row = row + row_offset
                    new_col = col + col_offset

                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                        neighbor_value = matrix[new_row][new_col]

                        if neighbor_value != 1:
                            neighbor_node = (new_row, new_col)
                            graph.add_edge(current_node, neighbor_node, weight=1)

    return graph


matriz_a_grafo = matrix_to_graph
