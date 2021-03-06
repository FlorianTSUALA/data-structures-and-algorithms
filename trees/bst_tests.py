from BST import BST
from BST import Node


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def test_BST():
    bst = BST()

    # Test empty tree
    assert (len(bst.BFS()) == 0)

    # Test insert
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    assert (len(bst.BFS()) == 3)
    expected = [2, 1, 3]
    actual = [node.value for node,l in bst.BFS()]
    assert_(expected, actual)

    # Test search
    assert(bst.search(2) is True)
    assert(bst.search(5) is False)

    # Test-1 Pre Order Traversal
    bst.insert(0)
    pre_order_expected = [2, 1, 0, 3]
    pre_order_actual = bst.pre_order_traversal()
    assert_(pre_order_expected, pre_order_actual)

    # Test-2 In-Order Traversal
    in_order_expected = [0, 1, 2, 3]
    in_order_actual = bst.in_order_traversal()
    assert_(in_order_expected, in_order_actual)

    # Test-3 Post-Order Traversal
    post_order_expected = [0, 1, 3, 2]
    post_order_actual = bst.post_order_traversal()
    assert_(post_order_expected, post_order_actual)

    # Test-4 Delete
    bst.delete(3)
    delete_expected_output = [0, 1, 2]
    delete_actual_output = bst.post_order_traversal()
    assert_(delete_expected_output, delete_actual_output)

    # Test-5 Delete
    bst.insert(5)
    bst.insert(4)
    bst.insert(8)
    bst.insert(6)
    bst.insert(9)
    delete_expected_output = [0, 1, 2, 4, 6, 8, 9]
    bst.delete(5)
    delete_actual_output = bst.in_order_traversal()
    assert_(delete_expected_output, delete_actual_output)

test_BST()