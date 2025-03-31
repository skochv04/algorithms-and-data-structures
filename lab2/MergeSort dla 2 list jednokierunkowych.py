#sortowanie 2 list do jednej
class Node:
    def __init__(self, value=0):
        self.val = value
        self.next = None

def merge_list (L1, L2):
    head1 = L1
    head2 = L2
    if L1.value < L2.value:
        start = L1
        start_head = start
        L1 = L1.next
    else:
        start = L2
        start_head = start
        L2 = L2.next
    start.next = None
    while L1 is not None and L2 is not None:
        if L1.value < L2.value:
            start.next = L1
            L1 = L1.next
        else:
            start.next = L2
            L2 = L2.next
        start = start.next
        start.next = None
    if L2 is None:
        start.next = L1
    else:
        start.next = L2
    return start.head


#sortowanie listy z seriami [1, 3, * 2, 4, 9, * 5]
# input typing
def separate (lst: Node)-> tuple[Node, Node]:
    p = lst
    while p.next is not None:
        if p.val > p.next.val:
            tmp = p.next
            p.next = None
            return lst, tmp
        p = p.next
    return lst, None


#L1 ma 2^n serii mat
def merge_sort(L1: Node)-> Node:
    while True:
        #gap?????????????
        L2 = Node()
        tail = L2
        # L2 = None
        counter = 0
        while L1 is not None:
            block1, L1 = separate(L1)
            block2, L1 = separate(L1)
            tail.next = merge_list(block1, block2)
            while tail.next is not None:
                tail = tail.next
            counter += 1
        if counter == 1:
            return L2
        L1 = L2