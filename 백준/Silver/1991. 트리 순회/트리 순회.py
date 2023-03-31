class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.data, end="")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end="")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end="")

def construct_tree(n, tree_data):
    tree_dict = {}
    for i in range(n):
        data, left, right = tree_data[i].split()
        if data not in tree_dict:
            tree_dict[data] = Node(data)
        if left != ".":
            if left not in tree_dict:
                tree_dict[left] = Node(left)
            tree_dict[data].left = tree_dict[left]
        if right != ".":
            if right not in tree_dict:
                tree_dict[right] = Node(right)
            tree_dict[data].right = tree_dict[right]
    return tree_dict['A']

n = int(input())
tree_data = []
for i in range(n):
    tree_data.append(input())

root = construct_tree(n, tree_data)

preorder_traversal(root)
print()
inorder_traversal(root)
print()
postorder_traversal(root)

"""
이진 트리를 구성하는 각 노드를 Node 클래스로 정의하고, 
이진 트리의 전위 순회, 중위 순회, 후위 순회 함수를 각각 preorder_traversal(), inorder_traversal(), postorder_traversal()로 정의합니다. 
그리고 construct_tree() 함수를 정의하여 입력값에 따라 이진 트리를 구성합니다. 

이진 트리의 루트 노드는 'A'로 고정되어 있으므로, tree_dict['A']를 반환합니다. 
입력값을 받은 후, construct_tree() 함수를 통해 이진 트리를 구성하고, 전위 순회, 중위 순회, 후위 순회 결과를 출력합니다.
"""