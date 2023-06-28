"""Тестирование алгоритмов."""
import pytest

from main.algorithms import (heap_sort, insertion_sort, merge_sort, quick_sort,
                             selection_sort)


class BasicTestSort:
    """Базовые тесты сортировок."""

    @pytest.fixture(autouse=True)
    def init_sorting_procedure(self, sorting_procedure):
        self.sorting_procedure = sorting_procedure

    def test_01_sort_empty_list(self):
        """Сортировка пустого списка."""
        data, result = [], []
        self.sorting_procedure(data)
        assert data == result

    def test_02_sort_one_item(self):
        """Сортировка списка с одним элементом."""
        data, result = [1], [1]
        self.sorting_procedure(data)
        assert data == result

    def test_03_sort_two_different_items(self):
        """Сортировка списка с двумя элементами (без повторений)."""
        data, result = [2, 1], [1, 2]
        self.sorting_procedure(data)
        assert data == result

    def test_04_sort_two_duplicate_items(self):
        """Сортировка списка с двумя элементами (с повторениями)."""
        data, result = [1, 1], [1, 1]
        self.sorting_procedure(data)
        assert data == result

    def test_05_sort_three_different_items(self):
        """Сортировка списка с тремя элементами (без повторений)."""
        data, result = [1, -1, 11], [-1, 1, 11]
        self.sorting_procedure(data)
        assert data == result

    def test_06_sort_three_duplicate_items(self):
        """Сортировка списка с тремя элементами (с повторениями)."""
        data, result = [1, -1, 1], [-1, 1, 1]
        self.sorting_procedure(data)
        assert data == result

    def test_07_sort_four_different_items(self):
        """Сортировка списка с четырьмя элементами (без повторений)."""
        data, result = [1, 111, -1, 11], [-1, 1, 11, 111]
        self.sorting_procedure(data)
        assert data == result

    def test_08_sort_four_duplicate_items(self):
        """Сортировка списка с четырьмя элементами (с повторениями)."""
        data, result = [1, -1, 11, 1], [-1, 1, 1, 11]
        self.sorting_procedure(data)
        assert data == result

    def test_09_sort_five_different_items(self):
        """Сортировка списка с пятью элементами (без повторений)."""
        data, result = [1111, 1, 111, -1, 11], [-1, 1, 11, 111, 1111]
        self.sorting_procedure(data)
        assert data == result

    def test_10_sort_five_duplicate_items(self):
        """Сортировка списка с пятью элементами (с повторениями)."""
        data, result = [1, 11, -1, 11, 1], [-1, 1, 1, 11, 11]
        self.sorting_procedure(data)
        assert data == result

    def test_11_sort_six_different_items(self):
        """Сортировка списка с шестью элементами (без повторений)."""
        data, result = [1111, 1, -11, 111, -1, 11], [-11, -1, 1, 11, 111, 1111]
        self.sorting_procedure(data)
        assert data == result

    def test_12_sort_six_duplicate_items(self):
        """Сортировка списка с шестью элементами (с повторениями)."""
        data, result = [1, 11, -1, 11, 1, 11], [-1, 1, 1, 11, 11, 11]
        self.sorting_procedure(data)
        assert data == result


@pytest.mark.parametrize('sorting_procedure', (insertion_sort,))
class Test01InsertionSort(BasicTestSort):
    """Тестирование алгоритма сортировки вставками."""

    pass


@pytest.mark.parametrize('sorting_procedure', (selection_sort,))
class Test02SelectionSort(BasicTestSort):
    """Тестирование алгоритма сортировки выбором."""

    pass


@pytest.mark.parametrize('sorting_procedure', (heap_sort,))
class Test03HeapSort(BasicTestSort):
    """Тестирование алгоритма сортировки вставками."""

    pass


@pytest.mark.parametrize('sorting_procedure', (merge_sort,))
class Test04MergeSort(BasicTestSort):
    """Тестирование алгоритма сортировки вставками."""

    pass


@pytest.mark.parametrize('sorting_procedure', (quick_sort,))
class Test05QuickSort(BasicTestSort):
    """Тестирование алгоритма сортировки вставками."""

    pass
