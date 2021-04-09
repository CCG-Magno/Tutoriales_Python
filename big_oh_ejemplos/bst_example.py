'''
In a balanced full binary tree,
 h = ⌈ log 2 ⁡ ( l ) ⌉ + 1 =

⌈ log 2 ⁡ ( ( n + 1 ) / 2 ) ⌉ + 1 =
⌈ log 2 ⁡ ( n + 1 ) ⌉ 

{\displaystyle 
h=⌈ \log _{2}(l)⌉ +1=
 ⌈ \log _{2}((n+1)/2)⌉ +1=
 ⌈ \log _{2}(n+1)⌉ } 
h=⌈ \log _{2}(l) ⌉ +1= 
⌈ \log _{2}((n+1)/2)⌉ +1=
⌈ \log _{2}(n+1)⌉ '''

# Python program to demonstrate  
# insert operation in binary search tree 
  
# A utility class that represents  
# an individual node in a BST 

class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert  
# a new node with the given key 
  
  
def insert(root, key): 
    if root is None: 
        return Node(key) 
    else: 
        if root.val == key: 
            return root 
        elif root.val < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root 
  
# A utility function to do inorder tree traversal 
  
  
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def preorder(root): 
    if root: 
        print(root.val) 
        preorder(root.left) 
        preorder(root.right) 

def postorder(root): 
    if root: 
        preorder(root.left) 
        preorder(root.right)
        print(root.val) 
  


def main():
    # Driver program to test the above functions 
    # Let us create the following BST 
    #    50 
    #  /     \ 
    # 30     70 
    #  / \ / \ 
    # 20 40 60 80 
    
    r = Node(50) 
    r = insert(r, 30) 
    r = insert(r, 20) 
    r = insert(r, 40) 
    r = insert(r, 70) 
    r = insert(r, 60) 
    r = insert(r, 80) 
    
    # Print inoder traversal of the BST 
    # inorder(r)
    preorder(r)
    # postorder(r)

if __name__ == "__main__":
    main()