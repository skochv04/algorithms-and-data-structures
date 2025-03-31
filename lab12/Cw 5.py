#Najlepsza ścieżka w drzewie

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.sum = None

def findMaxSum(root):
    res = float("-inf")

    def findMaxUtil(root):
        nonlocal res
        if root is None:
            return 0
        if root.sum != None:
            return root.sum
        l = findMaxUtil(root.left)
        r = findMaxUtil(root.right)
        max_single = max(max(l, r) + root.data, root.data)
        max_top = max(max_single, l + r + root.data)
        res = max(res, max_top)
        root.sum = max_single
        return root.sum

    findMaxUtil(root)
    return res

root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

print ("Max path sum is", findMaxSum(root))