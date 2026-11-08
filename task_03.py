import heapq
import math


def dijkstra(graph, start):
    if start not in graph:
        raise ValueError("Початкової вершини немає в графі.")
    if any(weight < 0 for neighbors in graph.values() for weight in neighbors.values()):
        raise ValueError("Ваги ребер мають бути невід’ємними.")

    distances = dict.fromkeys(graph, math.inf)
    previous = dict.fromkeys(graph)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance != distances[vertex]:
            continue

        for neighbor, weight in graph[vertex].items():
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = vertex
                heapq.heappush(queue, (candidate, neighbor))

    return distances, previous


def shortest_path(previous, start, target):
    path = []
    vertex = target
    while vertex is not None:
        path.append(vertex)
        if vertex == start:
            return path[::-1]
        vertex = previous[vertex]
    return []


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2},
        "E": {"C": 10, "D": 2},
        "F": {},
    }
    start = "A"
    distances, previous = dijkstra(graph, start)
    for vertex, distance in distances.items():
        path = shortest_path(previous, start, vertex)
        if path:
            print(f"{vertex}: {distance} ({' → '.join(path)})")
        else:
            print(f"{vertex}: недосяжна вершина")
