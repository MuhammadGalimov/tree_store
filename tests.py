from lib import TreeStore


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]


def test_create_tree_store():
    ts = TreeStore(items)


def test_get_all():
    ts = test_create_tree_store()

    assert ts.getAll() == items


def test_get_item():
    ts = test_create_tree_store()

    assert ts.getItem(7) == {"id": 7, "parent": 4, "type": None}


def test_get_children():
    ts = test_create_tree_store()

    assert ts.getChildren(4) == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    assert ts.getChildren(5) == []


def test_get_all_parents():
    ts = test_create_tree_store()

    assert ts.getAllParents(7) == [
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"}
    ]
