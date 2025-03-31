import queue
q = queue.PriorityQueue()
q.put(0, 10)
q.put(2, 144)
q.put(1, 166)
a = q.get()
print(a)
a = q.get()
print(a)
a = q.get()
print(a)


