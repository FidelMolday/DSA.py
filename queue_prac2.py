import queue

q = queue.LifoQueue()


numbers = [1,2,3,4,5,6,7]
for X in numbers:
    q.put(X)
    
 
print(q.get())   