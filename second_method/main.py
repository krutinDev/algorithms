

def bellman_ford(graph: dict[str, dict[str, int]], start: str, end: str) -> float | int:
    # Инициализация расстояний до всех вершин как бесконечность
    distances: dict[str, float] = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Итерации по ребрам графа
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Проверка на наличие отрицательных циклов
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return float('infinity')  # Отрицательный цикл обнаружен
    # Возвращение расстояния до конечной вершины
    return distances[end]


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
    shortest_path_length = bellman_ford(
        graph=main_graph,
        start='Санкт-Петербург',
        end='Владимир'
    )
    print(f"Длина кратчайшего пути: {shortest_path_length} км")
