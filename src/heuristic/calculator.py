def manhattan_distance(node_current, node_goal):
    return abs(node_current[0] - node_goal[0]) + abs(node_current[1] - node_goal[1])


def heuristic_table(graph, goal_node):
    heuristic = {}
    for node in graph.adjacency_list:
        heuristic[node] = manhattan_distance(node, goal_node)
    return heuristic


distancia_manhattan = manhattan_distance
generador_tabla_heuristica = heuristic_table