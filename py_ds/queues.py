from queue import Queue

q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print(q.full())
print(q.qsize())
for _ in range(q.qsize()):
    print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
#print(q.get_nowait())
print(q.empty())
