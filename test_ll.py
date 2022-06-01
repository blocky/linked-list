from ll import Node, LinkedList


def test_Node_init():
    n1 = Node('n1', None)
    n0 = Node('n0', n1)

    assert n0.data == 'n0'
    assert n0.succ == n1

    assert n1.data == 'n1'
    assert n1.succ is None


def test_Node_str():
    n1 = Node('n1', None)
    assert str(n1) == 'n1'


def test_LinkedList_add():
    lst = LinkedList()
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
    lst = LinkedList()
    n = lst.head
    assert n is None


def test_LinkedList_str():
    lst = LinkedList()
    lst.add('n0')
    lst.add('n1')
    assert str(lst) == "n1 -> n0 -> None"


def test_reverse_linked_list():
    lst = LinkedList()
    lst.add('n0')
    lst.add('n1')
    lst.add('n2')

    reversed_list = LinkedList.reverse_list(lst)

    # check the original list has not been modified
    n = lst.head
    assert n is not None
    assert n.data == "n2"
    n = n.succ
    assert n is not None
    assert n.data == "n1"
    n = n.succ
    assert n is not None
    assert n.data == "n0"
    assert n.succ is None

    # confirm the reversed list is ordered as expected
    n = reversed_list.head
    assert n is not None
    assert n.data == "n0"
    n = n.succ
    assert n is not None
    assert n.data == "n1"
    n = n.succ
    assert n is not None
    assert n.data == "n2"
    assert n.succ is None


def test_reverse_empty_linked_list():
    lst = LinkedList()
    reversed_list = LinkedList.reverse_list(lst)

    assert lst.head is None
    assert reversed_list.head is None
