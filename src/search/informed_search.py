import heapq
from src.heuristic.calculator import manhattan_distance


def a_star_search(graph, start, goal):
    start_heuristic = manhattan_distance(start, goal)
    frontier = [(start_heuristic, 0, [start])]
    g_costs = {start: 0}

    while frontier:
        _, current_cost, path = heapq.heappop(frontier)
        current_node = path[-1]

        if current_node == goal:
            return path

        for neighbor, edge_weight in graph.get_neighbors(current_node):
            new_cost = current_cost + edge_weight

            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                neighbor_heuristic = manhattan_distance(neighbor, goal)
                f_cost = new_cost + neighbor_heuristic
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(frontier, (f_cost, new_cost, new_path))

    return None


busqueda_a_estrella = a_star_search