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
        """Возвращает размер очереди."""
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


class Tree:
    """Бинарное дерево поиска."""

    LEFT_FLUG = 'left'
    RIGHT_FLUG = 'right'

    def __init__(self, value, left=None, right=None):
        """Конструктор бинарного дерева."""
        self.value = value
        self.left = left
        self.right = right

    def search(self, item):
        """Выполняет поиск элемента в бинарном дереве."""
        if self.value == item:
            return self

        if self.value > item and self.left:
            return self.left.search(item)

        if self.value < item and self.right:
            return self.right.search(item)

        return None

    def insert(self, item):
        """Выполняет вставку элемента в бинарное дерево."""
        if self.value == item:
            return

        object, attribute = (
            (self.left, self.LEFT_FLUG) if self.value > item else
            (self.right, self.RIGHT_FLUG)
        )
        object.insert(item) if object else setattr(self, attribute, Tree(item))

    def delete(self, item):
        """Выполняет удаление элемента из бинарного дерева."""
        if self.value > item and self.left:
            if self.left.value == item:
                return self._delete_child(self.LEFT_FLUG)
            self.left.delete(item)

        if self.value < item and self.right:
            if self.right.value == item:
                return self._delete_child(self.RIGHT_FLUG)
            self.right.dalete(item)

        return False

    def traverse_bfs(self):
        """Возвращает результат обхода бинарного дерева в ширину."""
        some_process = (lambda x: x)
        return [item for item in self._dfs(some_process)]

    def traverse_dfs(self):
        """Возвращает результат обхода бинарного дерева в глубину."""
        some_process = (lambda x: x)
        return [item for item in self._dfs(some_process)]

    def _delete_child(self, child_attr):
        """Выполняет удаление дочернего элемента."""
        child = getattr(self, child_attr)

        if not child.left and not child.right:
            setattr(self, child_attr, None)

        elif child.left and child.right:
            current = child.right

            while not current.left and current.right:
                current = current.right

            if not current.left:
                child.right.left = child.left
                setattr(self, child_attr, child.right)
            else:
                while current.left.left:
                    current = current.left
                child.value = current.left.value
                current.left = None

        elif child.left:
            setattr(self, child_attr, child.left)

        elif child.right:
            setattr(self, child_attr, child.right)

        return True

    def _bfs(self, some_process=print):
        """Выполняет обход бинарного дерева в ширину."""
        yield some_process(self.value)
        step_now = [self]

        while step_now:
            step_next = []

            for node in step_now:
                if node.left:
                    yield some_process(node.left.value)
                    step_next.append(node.left)

                if node.right:
                    yield some_process(node.right.value)
                    step_next.append(node.right)

            step_now = step_next

    def _dfs(self, some_process=print):
        """Выполняет обход бинарного дерева в глубину."""
        if self.left:
            self.left._dfs()

        yield some_process(self.value)

        if self.right:
            self.right._dfs()
