from collections import deque


def breadth_first_search(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current_node = path[-1]

        if current_node == goal:
            return path

        for neighbor, _ in graph.get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def depth_first_search(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        current_node = path[-1]

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, _ in graph.get_neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

    return None


busqueda_anchura = breadth_first_search
busqueda_profundidad = depth_first_search