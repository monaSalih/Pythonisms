from pythonism.pythonism import * 
import pytest 

def test_insert():
  # Arrange
  ll = LinkedList()
  ll.insert(5)
  ll.insert(2)
  ll.insert(25)
  expected = 25
  expected_ll = "{25}->{2}->{5}"
  # Actual
  actual = ll.head.data
  actual_ll = str(ll)
  # Assert
  assert actual == expected
  assert actual_ll == expected_ll

def test_ll_from_collection():
  ll = LinkedList([1,2])
  expected = "{1}->{2}"
  actual = str(ll)
  assert actual == expected

def test_iteration():
  ll = LinkedList([1,2])
  expected = [1,2]
  for index, actual_item in enumerate(ll):
    assert actual_item == expected[index]

def test_indexing():
  ll = LinkedList([1,2])
  expected_0 = 1
  expected_1 = 2
  actual_0 = ll[0]
  actual_1 = ll[1]
  assert actual_0 == expected_0
  assert actual_1 == expected_1
  with pytest.raises(IndexError, match="Index out of range"):
    actual = ll[2]


def test_product():
  # Arrange
  expected = 40
  #Act
  ll = LinkedList([1,5,2,4])
  actual = ll.find_product() 
  #Assert
  assert actual == expected 

def test_list():
  l1 =LinkedList()
  l1.insert(2)
  l1.insert(1)
  l1.insert(3)
  l1.insert(1)
  expected = [1,9,1,4]
  actual = l1.linked_list_squared()
  assert actual == expected
 
def test_math_sum():
  ll = LinkedList()
  node1 = Node(5)
  node2 = Node(10)
  node3 = Node(5)
  ll.head = node1
  node1.next = node2
  node2.next = node3
  expected = 20
  math = MathThings()
  ll.walk(math.adder)
  actual = math.sum
  assert expected == actual


def test_math_product():
  # Arrange
  expected = 40
  #Act
  ll = LinkedList()
  node1 = Node(1)
  node2 = Node(5)
  node3 = Node(2)
  node4 = Node(4)
  ll.head = node1
  node1.next = node2
  node2.next = node3
  node3.next = node4
  math = MathThings()
  ll.walk(math.multiplier)
  actual = math.product
  #Assert
  assert actual == expected 

def test_math_squared():
  l1 =LinkedList()
  l1.insert(2)
  l1.insert(1)
  l1.insert(3)
  l1.insert(1)
  expected = [1,9,1,4]
  math = MathThings()
  l1.walk(math.squared)
  actual = math.squares
  assert actual == expected
 

