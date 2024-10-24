import heapq


def dijkstra(graph: dict[str, dict[str, int]], start: str, end: str) -> float | int:
    # Инициализируем очередь с приоритетом с начальной вершиной
    queue: list[tuple[int, str]] = [(0, start)]
    # Словарь для хранения минимальных расстояний от начальной точки до каждой вершины
    distances: dict[str, float] = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        # Извлекаем вершину с минимальным расстоянием
        current_distance, current_node = heapq.heappop(queue)

        # Если достигли конечной вершины, возвращаем расстояние
        if current_node == end:
            return current_distance

        # Проверяем соседей текущей вершины
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Если найден более короткий путь к соседу, обновляем расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Добавляем соседа в очередь с приоритетом
                heapq.heappush(queue, (distance, neighbor))

    # Если путь не найден, возвращаем бесконечность
    return float('infinity')


# Определяем граф с городами и расстояниями между ними
main_graph: dict[str, dict[str, int]] = {
    'Санкт-Петербург': {'Великий Новгород': 151},
    'Великий Новгород': {'Санкт-Петербург': 151, 'Тверь': 323},
    'Тверь': {'Великий Новгород': 323, 'Москва': 156},
    'Москва': {
        'Тверь': 156, 'Смоленск': 363, 'Калуга': 157,
        'Тула': 171, 'Ярославль': 246, 'Владимир': 184
    },
    'Смоленск': {'Москва': 363},
    'Калуга': {'Москва': 157},
    'Тула': {'Москва': 171},
    'Ярославль': {'Москва': 246, 'Иваново': 100, 'Вологда': 174},
    'Иваново': {'Ярославль': 100, 'Владимир': 83},
    'Владимир': {'Иваново': 83, 'Москва': 184, 'Рязань': 192, 'Нижний Новгород': 224},
    'Нижний Новгород': {'Владимир': 224, 'Саранск': 217},
    'Саранск': {'Нижний Новгород': 217},
    'Рязань': {'Владимир': 192},
    'Вологда': {'Ярославль': 174}
}


if __name__ == "__main__":
    # Вычисляем длину кратчайшего пути от Санкт-Петербурга до Владимира
    # main_graph['Москва']['Владимир'] = 200 -> Если будет желание изменить длину пути :)
    shortest_path_length = dijkstra(
        graph=main_graph,
        start='Санкт-Петербург',
        end='Владимир'
    )
    print(f"Длина кратчайшего пути: {shortest_path_length} км")