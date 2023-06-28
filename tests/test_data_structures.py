"""Тестирование структур данных."""
import pytest

from main.data_structures import Heap, Queue, Stack, Tree


class Test01Heap:
    """Тестирование структуры данных «Пирамида»."""

    def test_01_init(self):
        test = [
            [Heap([]), []],
            [Heap([1]), [1]],
            [Heap([2, 1]), [1, 2]],
            [Heap([3, 2, 1]), [1, 2, 3]],
            [Heap([3, 1, 2]), [1, 3, 2]],
            [Heap([3, 1, 4, 2]), [1, 2, 4, 3]],
            [Heap([4, 2, 1, 3]), [1, 2, 4, 3]],
            [Heap([4, 1, 2, 3]), [1, 3, 2, 4]]
        ]
        for heap, data in test:
            assert heap.data == data

    def test_02_insert(self):
        test = [
            [Heap([]), [1]],
            [Heap([1]), [1, 1]],
            [Heap([2, 1]), [1, 2, 1]],
            [Heap([3, 2, 1]), [1, 1, 3, 2]],
            [Heap([3, 1, 2]), [1, 1, 2, 3]],
            [Heap([4, 2, 1, 3]), [1, 1, 4, 3, 2]],
            [Heap([3, 1, 4, 2]), [1, 1, 4, 3, 2]],
            [Heap([4, 1, 2, 3]), [1, 1, 2, 4, 3]]
        ]
        for heap, next_data in test:
            heap.insert(1)
            assert heap.data == next_data

    def test_03_extract_min(self):
        with pytest.raises(IndexError, match='extract_min from empty heap'):
            Heap([]).extract_min()

        test = [
            [Heap([1]), 1],
            [Heap([2, 1]), 1],
            [Heap([3, 2, 1]), 1],
            [Heap([3, 1, 2]), 1],
            [Heap([3, 1, 4, 2]), 1],
            [Heap([4, 2, 1, 3]), 1],
            [Heap([4, 1, 2, 3]), 1]
        ]
        for heap, min_item in test:
            assert heap.extract_min() == min_item

    def test_04_head(self):
        with pytest.raises(IndexError, match='head from empty heap'):
            Heap([]).head()

        test = [
            [Heap([1]), 1],
            [Heap([2, 1]), 1],
            [Heap([3, 2, 1]), 1],
            [Heap([3, 1, 2]), 1],
            [Heap([3, 1, 4, 2]), 1],
            [Heap([4, 2, 1, 3]), 1],
            [Heap([4, 1, 2, 3]), 1]
        ]
        for heap, head_item in test:
            assert heap.head() == head_item


class Test02Queue:
    """Тестирование структуры данных «Очередь»."""

    def test_01_init(self):
        test = [
            [Queue(list()),
                [[Queue.DEFAULT_ITEM for _ in range(Queue.MIN_SIZE)]]],
            [Queue(list(range(50))),
                [list(range(50)) +
                    [Queue.DEFAULT_ITEM] * (Queue.MIN_SIZE - 50)]],
            [Queue(list(range(50)), 20),
                [list(range(20)), list(range(20, 40)), list(range(40, 50)) +
                    [Queue.DEFAULT_ITEM] * 10]],
            [Queue(list(range(150))),
                [list(range(150)),
                    [Queue.DEFAULT_ITEM] * 150]]
        ]
        for queue, data in test:
            assert queue.data == data

    def test_02_clear(self):
        test = [
            [Queue(list()),
                [[Queue.DEFAULT_ITEM for _ in range(Queue.MIN_SIZE)]]],
            [Queue(list(range(50)), 20),
                [[Queue.DEFAULT_ITEM for _ in range(20)]]]
        ]
        for queue, next_data in test:
            queue.clear()
            assert queue.data == next_data

    def test_03_pop(self):
        with pytest.raises(IndexError, match='pop from empty queue'):
            Queue(list()).pop()

        test = [
            [Queue(list(range(5))), 0, 1],
            [Queue(list(range(5)), 1), 0, 1]
        ]
        for queue, pop_result, next_pop_result in test:
            assert queue.pop() == pop_result
            assert queue.pop() == next_pop_result

    def test_04_push(self):
        push_item = 'test'
        test = [
            [Queue(list(range(4)), 5),
                [[0, 1, 2, 3, push_item],
                    [Queue.DEFAULT_ITEM for _ in range(5)]]],
            [Queue(list(range(5)), 1),
                [[0], [1], [2], [3], [4], [push_item],
                    [Queue.DEFAULT_ITEM]]]
        ]
        for queue, next_data in test:
            queue.push(push_item)
            assert queue.data == next_data

    def test_05_front(self):
        with pytest.raises(IndexError, match='front from empty queue'):
            Queue(list()).front()

        test = [
            [Queue(list(range(5))), 0, 1],
            [Queue(list(range(5)), 1), 0, 1]
        ]
        for queue, front_result, front_result_before_pop in test:
            assert queue.front() == front_result
            queue.pop()
            assert queue.front() == front_result_before_pop


class Test03Stack:
    """Тестирование структуры данных «Стэк»."""

    def test_01_init(self):
        test = [
            [Stack(list()), list()],
            [Stack(list(range(5))), list(range(5))]
        ]
        for stack, data in test:
            assert stack.data == data

    def test_02_clear(self):
        test = [
            [Stack(list()), list()],
            [Stack(list(range(5))), list()]
        ]
        for stack, data in test:
            stack.clear()
            assert stack.data == data

    def test_03_pop(self):
        with pytest.raises(IndexError, match='pop from empty stack'):
            Stack(list()).pop()

        test = [
            [Stack(list(range(2))), 1, 0],
            [Stack(list(range(5))), 4, 3]
        ]
        for stack, pop_result, next_pop_result in test:
            assert stack.pop() == pop_result
            assert stack.pop() == next_pop_result

    def test_04_push(self):
        push_item = 'test'
        test = [
            [Stack(list()), [push_item]],
            [Stack(list(range(5))), list(range(5)) + [push_item]]
        ]
        for stack, next_data in test:
            stack.push(push_item)
            assert stack.data == next_data

    def test_05_back(self):
        with pytest.raises(IndexError, match='back from empty stack'):
            Stack(list()).back()

        test = [
            [Stack(list(range(2))), 1, 0],
            [Stack(list(range(5))), 4, 3]
        ]
        for stack, back_result, back_result_before_pop in test:
            assert stack.back() == back_result
            stack.pop()
            assert stack.back() == back_result_before_pop


@pytest.mark.usefixtures('init_tree')
class Test04Tree:
    """Тестирование структуры данных  «Бинарное дерево поиска»."""

    def test_01_init(self):
        with pytest.raises(TypeError):
            Tree()

        test = [
            [Tree(2), 2, None, None],
            [Tree(2, Tree(1)), 2, 1, None],
            [Tree(2, Tree(1), Tree(3)), 2, 1, 3]
        ]
        for tree, value, left_val, right_val in test:
            assert tree.value == value
            assert tree.left.value if tree.left else tree.left == left_val
            assert tree.right.value if tree.right else tree.right == right_val

    def test_02_insert(self):
        tree = Tree(5)
        test = [
            [tree.insert(3), tree, 5, 3, None],
            [tree.insert(8), tree, 5, 3, 8],
            [tree.insert(7), tree.right, 8, 7, None],
            [tree.insert(9), tree.right, 8, 7, 9],
            [tree.insert(2), tree.left, 3, 2, None],
            [tree.insert(4), tree.left, 3, 2, 4]
        ]
        for op, tree, value, left_val, right_val in test:
            assert tree.value == value
            assert tree.left.value if tree.left else tree.left == left_val
            assert tree.right.value if tree.right else tree.right == right_val

    def test_03_delete(self):
        tree = Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(7), Tree(9)))

        with pytest.raises(KeyError):
            tree.delete(5)

        test = [
            [tree.delete(8), tree, 5, 3, 9],
            [tree.delete(9), tree, 5, 3, 7],
            [tree.delete(2), tree.left, 3, None, 4]
        ]
        for op, tree, value, left_val, right_val in test:
            assert tree.value == value
            assert tree.left.value if tree.left else tree.left == left_val
            assert tree.right.value if tree.right else tree.right == right_val

    def test_04_search(self):
        test = [
            [self.tree.search(5), 5, 3, 8],
            [self.tree.search(3), 3, 2, 4],
            [self.tree.search(7), 7, None, None],
            [self.tree.search(4), 4, None, None]
        ]
        for res, value, left_val, right_val in test:
            assert res.value == value
            assert res.left.value if res.left else res.left == left_val
            assert res.right.value if res.right else res.right == right_val
        assert self.tree.search(10) is None

    def test_05_traverse_bfs(self):
        assert self.tree.traverse_bfs() == [5, 3, 8, 2, 4, 7, 9]

    def test_06_traverse_dfs(self):
        assert self.tree.traverse_dfs() == [2, 3, 4, 5, 7, 8, 9]
