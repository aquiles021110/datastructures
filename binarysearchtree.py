class node:
    def __init__(self,m):
        self.data=m
        self.right_node=None
        self.left_node=None
def inordertraversal(root):
    if root is not None:
        if root.left_node is not None:
            inordertraversal(root.left_node)
        print(root.data)
        if root.right_node is not None:
            inordertraversal(root.right_node)
def insert(root,x):
    if root is None:
        return node(x)
    if x<root.data:
        root.left_node=insert(root.left_node,x)
    else:
        root.right_node=insert(root.right_node,x)
    return root
def inordersuccesor(root):
    current=root
    while current.left_node is not None:
        current=current.left_node
    return current
def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left_node=delete(root.left_node,key)
    if key>root.data:
        root.right_node=delete(root.right_node,key)
    else:
        if root.left_node is None:
            right=root.right_node
            root=None
            return right
        elif root.right_node is None:
            left=root.left_node
            root=None
            return left
        else:
            temp=inordersuccesor(root)
            print('Hi',temp.data)
            tem2=root.data
            root.data=temp.data
            temp.data=tem2
            root.right_node=delete(root.right_node,temp.data)
elements=int(input('How many elements in the tree? '))
root=None
for i in range(elements):
    n1=int(input('Enter node value: '))
    root=insert(root,n1)
inordertraversal(root)
print('Deleting from case one')
va=delete(root,3)
inordertraversal(va)
print('Deleting from case two')
vb=delete(root,5)
inordertraversal(vb)
print('Deleting a node with two children case three')
vc=delete(root,10)
inordertraversal(vc)
