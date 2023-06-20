"""Структуры даннных."""


class Heap:
    """Пирамида.

    Создание структуры данных: time - O(N), memory - O(N);
    Вставка/удаление элемента: time - O(log(N)), memory - O(1),
                               где N = len(self.data).
    """

    def __init__(self, data: list):
        """Конструктор пирамиды."""
        self.data = data
        self.size = len(data)

        for idx in range(self.size // 2 - 1, -1, -1):
            parent_idx, min_idx = idx, self._min_in_cluster(idx)
            if parent_idx != min_idx:
                self.data[parent_idx], self.data[min_idx] = (
                    self.data[min_idx], self.data[parent_idx]
                )

    @staticmethod
    def _parent(item_idx: int):
        """По индексу дочернего элемента возвращает индекс родительского."""
        if item_idx < 0:
            raise Exception('Value is non-positive.')
        return (item_idx - 1) // 2 if item_idx else None

    def _min_in_cluster(self, item_idx: int):
        """Возвращает индекс наименьшего элемента в кластере родитель-дети."""
        if item_idx * 2 + 2 < self.size:
            return min(item_idx, item_idx * 2 + 1, item_idx * 2 + 2,
                       key=(lambda x: self.data[x]))
        if item_idx * 2 + 1 < self.size:
            return min(item_idx, item_idx * 2 + 1,
                       key=(lambda x: self.data[x]))
        return item_idx

    def insert(self, item):
        """Выполняет вставку элемента в пирамиду."""
        self.data.append(item)

        item_idx, parent_idx = self.size, self._parent(self.size)
        while parent_idx and self.data[item_idx] < self.data[parent_idx]:
            self.data[item_idx], self.data[parent_idx] = (
                self.data[parent_idx], self.data[item_idx]
            )
            item_idx, parent_idx = parent_idx, self._parent(parent_idx)

        self.size += 1

    def extract_min(self):
        """Выполняет удаление наименьшего (верхнего) элемента пирамиды."""
        if not self.size:
            raise Exception('Heap is empty.')
        self.data[0] = min_item = self.data.pop()

        parent_idx, min_idx = 0, self._min_in_cluster(0)
        while parent_idx != min_idx:
            self.data[parent_idx], self.data[min_idx] = (
                self.data[min_idx], self.data[parent_idx]
            )
            parent_idx, min_idx = min_idx, self._min_in_cluster(min_idx)

        self.size -= 1
        return min_item
