from lib import TreeStore, RequiredFieldsException, UniqueIdException

import pytest


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
    _ = TreeStore(items)

def test_create_wrong_tree_1():
    with pytest.raises(RequiredFieldsException):
        _ = TreeStore([
            {"id": 1, "parent": "root"},
            {"id": 2, "type": "test"}
        ])

def test_create_wrong_tree_2():
    with pytest.raises(RequiredFieldsException):
        _ = TreeStore([
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            [3, 1],
        ])

def test_create_wrong_tree_3():
    with pytest.raises(UniqueIdException):
        _ = TreeStore([
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 2, "parent": 1, "type": "test2"},
        ])

def test_get_all():
    ts = TreeStore(items)

    assert ts.getAll() == items


def test_get_item():
    ts = TreeStore(items)

    assert ts.getItem(7) == {"id": 7, "parent": 4, "type": None}


def test_get_children():
    ts = TreeStore(items)

    assert ts.getChildren(4) == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    assert ts.getChildren(5) == []


def test_get_all_parents():
    ts = TreeStore(items)

    assert ts.getAllParents(7) == [
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"}
    ]
