class Node:
    def __init__(self, value = 0):
        self.val = value
        self.left = None
        self.right = None

def print_out(p):

    if p != None:
        print(p.val)
        print_out(p.left)
        print_out(p.right)

def member_BST(p, n):
    if p == None:
        return False
    if p.val == n:
        return True
    return p.member_BST(p.left, n) if n < p.val else p.member_BST(p.right, n)

def insert_BST(p, n):
    if p == None:
        p = Node(n)
        return p
    if p.val == n:
        return p
    if p.val > n:
        p.left = insert_BST(p.left, n)
    if p.val < n:
        p.right = insert_BST(p.right, n)
    return p


def deleteNode(root, k):
    if root is None:
        return root

    if root.val > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.val < k:
        root.right = deleteNode(root.right, k)
        return root

    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp


    else:
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.right = succ.right
        root.val = succ.val
        del succ
        return root


T = Node()
insert_BST(T, 24)
insert_BST(T, 28)
insert_BST(T, 11)
print_out(T)
print()
deleteNode(T, 24)
print_out(T)