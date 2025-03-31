# We are given three strings A, B and C. A and B are of the same length. The following properties apply:
#   1) Letters at the sane index in strings A and B are equivalent
#   2) If letter a is equivalent with letter b, then letter b is equivalent with letter a
#   3) If letter a is equivalent with letter b and letter b is equivalent with letter c, then letter
#      a is equivalent to letter c
#   4) Each letter is equivalent to itself
# In string C we can replace any letter with a letter equivalent to it. What is the smallest
# lexicographically string that we can create in this way?

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self

def make_set(val):
    return Node(val)

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def equivalent_letters(A, B, C):
    N = len(A)
    A = [ord(A[i]) for i in range(N)]
    B = [ord(B[i]) for i in range(N)]
    a = b = A[0]
    for i in range(N):
        a = min(a, A[i], B[i])
        b = max(b, A[i], B[i])
    s = 97
    n = (b - a) + 1
    letters = [None for _ in range(n)]

    for i in range(len(A)):
        if letters[A[i] - 97] is not None and letters[B[i] - 97] is not None:
            x = letters[A[i] - 97]
            y = letters[B[i] - 97]
        elif letters[A[i] - 97] is not None and letters[B[i] - 97] is None:
            x = letters[A[i] - 97]
            y = make_set(B[i])
            letters[B[i] - 97] = y
        elif letters[A[i] - 97] is None and letters[B[i] - 97] is not None:
            x = make_set(A[i])
            letters[A[i] - 97] = x
            y = letters[B[i] - 97]
        else:
            x = make_set(A[i])
            letters[A[i] - 97] = x
            y = make_set(B[i])
            letters[B[i] - 97] = y
        if A[i] > B[i]:
            union(x, y)
        else:
            union(y, x)
    word = [C[i] for i in range(len(C))]
    for i in range(len(C)):
        if letters[ord(C[i]) - 97] is not None:
            x = letters[ord(C[i]) - 97]
            while x != x.parent:
                x = x.parent
            word[i] = chr(x.value)
    new_word = ''
    for i in range(len(C)):
        new_word += word[i]
    return new_word

A = "caef"
B = "fbga"
C = "abdfe"

print(equivalent_letters(A, B, C))