def process_maze(file_path):
    matrix = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith('(') and line.endswith(')'):
                continue

            clean_line = line.replace('[', ' ').replace(']', ' ').replace(',', ' ').replace('(', ' ').replace(')', ' ')
            cells = clean_line.split()

            if cells:
                row = [int(cell) for cell in cells]
                matrix.append(row)

    if not matrix:
        return matrix, 0, 0, None, None

    rows = len(matrix)
    cols = len(matrix[0])
    start = None
    goal = None

    for i in range(rows):
        for j in range(cols):
            value = matrix[i][j]
            if value == 2:
                start = (i, j)
            elif value == 3:
                goal = (i, j)

    return matrix, rows, cols, start, goal


procesar_laberinto = process_maze