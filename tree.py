class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(root, data):
  if root is None:
    root = Node(data)
    return root
  else:
    if data < root.data:
      root.left = insert(root.left, data)
    else:
      root.right = insert(root.right, data)
  return root

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

# Contoh penggunaan
root = None
root = insert(root, 10)
insert(root, 5)
insert(root, 15)
inorder_traversal(root)  # Output: 5 10 15
