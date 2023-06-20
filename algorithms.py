"""Алгоритмы."""


def insertion_sort(data: list) -> None:
    """Сортировка вставками."""
    for cur in range(len(data) - 1):
        for j in range(cur, -1, -1):
            if data[j] < data[j + 1]:
                break
            data[j], data[j + 1] = data[j + 1], data[j]


def selection_sort(data: list) -> None:
    """Сортировка методом выбора."""
    for cur in range(len(data)):
        min = cur
        for j in range(cur, len(data)):
            if data[j] < data[min]:
                min = j
        data[cur], data[min] = data[min], data[cur]
