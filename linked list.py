class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = Node(data)

  def remove_at_beginning(self):
    if self.head is None:
      return None
    else:
      data = self.head.data
      self.head = self.head.next
      return data

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next

# Contoh penggunaan
linked_list = LinkedList()
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(5)
linked_list.insert_at_end(20)
linked_list.print_list()  # Output: 5 10 20
linked_list.remove_at_beginning()
linked_list.print_list()  # Output: 10 20
