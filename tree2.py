class tree:
    def __init__(self,x):
        self.data=x
        self.left_node=None
        self.right_node=None
def Inordertraversal(root):
    if root is not None:
        if root.left_node is not None:
            Inordertraversal(root.left_node)
        print(root.data)
        if root.right_node is not None:
            Inordertraversal(root.right_node)
def Insert(root,k):
    if root==None:
        return tree(k)
    if root.data>k:
        root.left_node=Insert(root.left_node,k)
    else:
        root.right_node=Insert(root.right_node,k)
    return root
def Search(root,key):
    if root.data==key:
        return root
    elif root.data>key and root.left_node is not None:
        return Search(root.left_node,key)
    elif root.data<key and root.right_node is not None:
        return Search(root.right_node,key)
    else:
        return -1
n=int(input('Number of elements in tree: '))
root=None
for i in range(n):
    x=int(input('Input node value: '))
    root=Insert(root,x)
Inordertraversal(root)
key=int(input('Input search element: '))
keynode=Search(root,key)
if keynode==-1:
    print('Key does not exsist')
else:
    print(f'Key is {keynode.data}')
