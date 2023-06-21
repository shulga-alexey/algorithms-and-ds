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
            return min(
                item_idx, item_idx * 2 + 1, item_idx * 2 + 2,
                key=(lambda x: self.data[x])
            )

        if item_idx * 2 + 1 < self.size:
            return min(
                item_idx, item_idx * 2 + 1,
                key=(lambda x: self.data[x])
            )

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

    def head(self):
        """Возвращает минимальный (верхний) элемент пирамиды."""
        return self.data[0]


class Queue:
    """Очередь."""

    def __init__(self, data, size_of_cluster=None):
        """Конструктор очереди."""
        self.upper = -1
        self.data = [data, []]
        self.size_of_cluster = size_of_cluster or len(data)

    def clear(self):
        """Очищает очередь."""
        self.upper = -1
        self.data = [[]]

    def pop(self):
        """Выполняет извлечение и удаление элемента из начала очереди."""
        self.upper += 1

        if self.upper == self.size_of_cluster:
            self.upper = 0
            self.data.pop(0)

        if not self.data[0] or self.upper >= len(self.data[0]):
            raise Exception('Queue is empty.')

        return self.data[0][self.upper]

    def push(self, item):
        """Выполняет вставку элемента в конец очереди."""
        if len(self.data[-1]) == self.size_of_cluster:
            self.data.append([])

        self.data[-1].append(item)

    def front(self):
        """Возвращает первый элемент очереди, не удаляя его."""
        front = self.upper + 1

        if front >= len(self.data[0]):
            raise Exception('Queue is empty.')

        return self.data[0][front]

    @property
    def size(self):
        """Возвращает размер стэка."""
        start = len(self.data[0]) - (self.upper + 1)
        core = (
            (len(self.data) - 2 if len(self.data) - 2 > 0 else 0) *
            self.size_of_cluster
        )
        end = 0 if not len(self.data) else len(self.data[-1])

        return start + core + end

    @property
    def is_empty(self):
        """Определяет пуста ли очередь."""
        return not bool(self.size)


class Stack:
    """Стэк."""

    def __init__(self, data):
        """Конструктор стэка."""
        self.data = data

    def clear(self):
        """Очищает стэк."""
        self.data = []

    def back(self):
        """Возвращает верхний элемент стэка, не удаляя его."""
        if not self.data:
            raise Exception('Stack is empty.')

        return self.data[-1]

    def pop(self):
        """Выполняет извлечение и удаление верхнего элемента стэка."""
        if not self.data:
            raise Exception('Stack is empty.')

        return self.data.pop()

    def push(self, item):
        """Выполняет вставку элемента на верх стэка."""
        self.data.append(item)

    @property
    def size(self):
        """Возвращает размер стэка."""
        return len(self.data)
