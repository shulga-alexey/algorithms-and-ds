import pytest

from main.data_structures import Tree


@pytest.fixture(scope='class')
def init_tree(request):
    request.cls.tree = (
        Tree(5, Tree(3, Tree(2), Tree(4)), Tree(8, Tree(7), Tree(9)))
    )
