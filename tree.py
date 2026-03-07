class tree:
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None

def inordertraversal(root):
    if root.left_node!=None:
        inordertraversal(root.left_node)
    print(root.data)
    if root.right_node!=None:
        inordertraversal(root.right_node)

def preorderedtraversal(root):
    print(root.data)
    if root.left_node!=None:
        preorderedtraversal(root.left_node)
    if root.right_node!=None:
        preorderedtraversal(root.right_node)

def postorderedtraversal(root):
    if root.left_node!=None:
        postorderedtraversal(root.left_node)
    if root.right_node!=None:
        postorderedtraversal(root.right_node)
    print(root.data)

root=tree(5)
root.left_node=tree(4)
root.right_node=tree(6)
root.left_node.left_node=tree(7)
root.left_node.right_node=tree(8)
root.right_node.left_node=tree(9)
root.right_node.right_node=tree(10)
postorderedtraversal(root)
print('####')
#hw
'''Count the Nodes
Task: Create a function to count the total number of nodes present in a given tree.
Input: A tree with a root node (e.g., Root=10, Left=5, Right=15).
Goal: Output: 3.
Logic (Give If Needed):
Base Case: If root is None, return 0.
Recursive Step: Return 1 + count_nodes(root.left) + count_nodes(root.right). 
This adds the current node (1) to the total nodes found in the left and right subtrees.'''
def count_nodes(root):
    if root==None:
        return 0
    else:
        return 1 + count_nodes(root.left_node) + count_nodes(root.right_node)
print(f'There are {count_nodes(root)} nodes in this tree.')
print('####')
'''Find the Maximum Value
Task: Find the largest integer value stored in a binary tree.
Input: A tree with various integer values (e.g., 10, 20, 5).
Goal: Output: 20.
Logic (Give If Needed):
Base Case: If root is None, return a very small number (e.g., -1000).
Recursive Step: Find the max in the left child and the max in the right child.
Compare root.data, left_max, and right_max and return the highest of the three.'''
def max_val(root):
    if root==None:
        return -1000000
    leftmax=max_val(root.left_node)
    rightmax=max_val(root.right_node)
    return max(root.data,leftmax,rightmax)
print(max_val(root))