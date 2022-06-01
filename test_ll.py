import ll


def test_Node_init():
    n1 = ll.Node('n1', None)
    n0 = ll.Node('n0', n1)

    assert n0.data == 'n0'
    assert n0.succ == n1

    assert n1.data == 'n1'
    assert n1.succ is None


def test_Node_str():
    n1 = ll.Node('n1', None)
    assert str(n1) == 'n1'


def test_LinkedList_add():
    lst = ll.LinkedList()
    lst.add('n0')

    n = lst.head
    assert n.data == 'n0'
    assert n.succ is None

    lst.add('n1')
    n = lst.head
    assert n.data == 'n1'
    assert n.succ is not None
    assert n.succ.data == 'n0'


def test_LinkedList_head_when_empty():
    lst = ll.LinkedList()
    n = lst.head
    assert n is None


def test_LinkedList_str():
    lst = ll.LinkedList()
    lst.add('n0')
    lst.add('n1')
    assert str(lst) == "n1 -> n0 -> None"
