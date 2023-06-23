"""Тестирование алгоритмов."""

from main.algorithms import (heap_sort, insertion_sort, merge_sort, quick_sort,
                             selection_sort)


class Test01InsertionSort:
    """Тестирование алгоритма сортировки вставками."""

    def test_01_insertion_sort(self):
        """Сортировка пустого списка."""
        data, result = [], []
        insertion_sort(data)
        assert data == result

    def test_02_insertion_sort(self):
        """Сортировка списка с одним элементом."""
        data, result = [1], [1]
        insertion_sort(data)
        assert data == result

    def test_03_insertion_sort(self):
        """Сортировка списка с двумя элементами (без повторений)."""
        data, result = [2, 1], [1, 2]
        insertion_sort(data)
        assert data == result

    def test_04_insertion_sort(self):
        """Сортировка списка с двумя элементами (с повторениями)."""
        data, result = [1, 1], [1, 1]
        insertion_sort(data)
        assert data == result

    def test_05_insertion_sort(self):
        """Сортировка списка с тремя элементами (без повторений)."""
        data, result = [1, -1, 11], [-1, 1, 11]
        insertion_sort(data)
        assert data == result

    def test_06_insertion_sort(self):
        """Сортировка списка с тремя элементами (с повторениями)."""
        data, result = [1, -1, 1], [-1, 1, 1]
        insertion_sort(data)
        assert data == result

    def test_07_insertion_sort(self):
        """Сортировка списка с четырьмя элементами (без повторений)."""
        data, result = [1, 111, -1, 11], [-1, 1, 11, 111]
        insertion_sort(data)
        assert data == result

    def test_08_insertion_sort(self):
        """Сортировка списка с четырьмя элементами (с повторениями)."""
        data, result = [1, -1, 1, 11], [-1, 1, 1, 11]
        insertion_sort(data)
        assert data == result

class Test02SelectionSort:
    """Тестирование алгоритма сортировки выбором."""
    
    pass


class Test03HeapSort:
    """Тестирование алгоритма сортировки вставками."""

    pass


class Test04MergeSort:
    """Тестирование алгоритма сортировки вставками."""

    pass


class Test05QuickSort:
    """Тестирование алгоритма сортировки вставками."""

    pass
