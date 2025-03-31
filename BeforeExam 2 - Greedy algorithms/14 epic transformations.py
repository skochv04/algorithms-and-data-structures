# We are given an array a of length n consisting of integers. We can apply the following operation,
# consisting of several steps, on the array a zero or more times:
# - we select two different numbers in the array a[i] and a[j],
# - we remove i-th and j-th elements from the array.
# For example, if n=6 and a=[1, 6, 1, 1, 4, 4], then you can perform the following sequence of operations:
# - select i=1,j=5. The array a becomes equal to [6, 1, 1, 4],
# - select i=1,j=2. The array a becomes equal to [1, 4].
# What can be the minimum size of the array after applying some sequence of operations to it?

def epic_transformation(T, n):
    max_el = 0
    for el in T:
        max_el = max(max_el, el)
    tab = [0 for _ in range(max_el + 1)]
    for el in T:
        tab[el] += 1
    max_amount = 0
    print(tab)
    for j in range(max_el + 1):
        max_amount = max(max_amount, tab[j])
    if n - max_amount < max_amount:
        return max_amount - (n - max_amount)
    else:
        return n % 2


T = [6, 6, 4, 4, 6, 6, 4, 6, 4]
print(epic_transformation(T, len(T)))