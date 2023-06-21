"""Алгоритмы."""
import math
import random

from data_structures import Heap, Queue


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


def heap_sort(data: list) -> None:
    """Пирамидальная сортировка."""
    heap = Heap(data)
    for i in range(len(data)):
        data[i] = heap.extract_min()


def merge_sort(data: list) -> None:
    """Сортировка слиянием."""
    for i in range(int(math.log(len(data), 2))):
        base = 2 ** i
        for j in range(0, len(data), base * 2):
            queue1, queue2 = (
                Queue(data[base * j: base * (j + 1)]),
                Queue(data[base * (j + 1): base * (j + 2)])
            )
            for k in range(base * j, min(base * (j + 2), len(data))):
                min_queue = (
                    (queue1 if queue2.is_empty else None) or
                    (queue2 if queue1.is_empty else None) or
                    min(queue1, queue2, key=(lambda x: x.front()))
                )
                data[k] = min_queue.pop()


def quick_sort(data: list) -> None:
    """Быстрая сортировка."""
    def quick_recursion(data=data, start=0, end=len(data)):
        if start < end:
            check_idx = random.randint(start, end - 1)

            pivot_idx = start if check_idx != start else start + 1
            for idx in range(start + 1, end):
                if data[check_idx] > data[idx]:
                    data[pivot_idx], data[idx] = data[idx], data[pivot_idx]
                    pivot_idx += 1 if check_idx != pivot_idx + 1 else 2

            pivot_idx -= 0 if data[check_idx] > data[pivot_idx] else 1
            data[check_idx], data[pivot_idx] = (
                data[pivot_idx], data[check_idx]
            )

            quick_recursion(data, start, pivot_idx)
            quick_recursion(data, pivot_idx + 1, end)

    quick_recursion()
