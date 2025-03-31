# In one of the Chinese provinces, it was decided to build a series of machines to protect the
# population against the coronavirus. The province can be visualized as an array of values 1 and 0,
# which arr[i] = 1 means that in city [i] it is possible to build a machine and value 0 that it can't.
# There is also a number k, which means that if we put the machine in the city [i], then the cities with
# indices [j] such that that abs(i-j) < k are through it protected. Find the minimum number of machines
# are needed to provide security in each city, or -1 if that is impossible.

def machines_saving_people(T, k):
    n = len(T)
    count = 0
    last = -1
    pos = last + k
    while last + k < n:
        if pos > n - 1:
            pos = n - 1
        while T[pos] == 0 and pos >= last + 1:
            pos -= 1
        if pos == last:
            return -1
        last = pos
        pos += 2 * k - 1
        count += 1
    return count

T = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
k = 4
print(machines_saving_people(T, k))