# First In First Out (FIFO)

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    if len(q) < 1:
        return None
    q.pop(0)
    
def displayQueue(q):
    print(q)

def lengthQueue(q):
    return len(q)


testQueue = []

enqueue(testQueue, 4)
displayQueue(testQueue)
lengthQueue(testQueue)

enqueue(testQueue, 8)
displayQueue(testQueue)

dequeue(testQueue)
displayQueue(testQueue)


"""
Operations:
1. Enqueue - Add element to the end
2. Dequeue - Remove element from the front
3. isEmpty
4. isFull
5. Peek


"""