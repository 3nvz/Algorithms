# Last In First Out (LIFO)
# O(1) time complexity


def cerateStack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False
    
def push(stack, item):
    stack.append(item)
    print("Item ", item, " was pushed on the stack")

def pop(stack):
    if isEmpty(stack):
        return "Stack is empty"
    stack.pop()
    
newStack = cerateStack()
push(newStack, 3)
print("Content of new stack: ", newStack)

print(isEmpty(newStack))

pop(newStack)
print("New stack after popping", newStack)



"""

Basic Operations:
1. Push
2. Pop
3. isEmpty
4. isFull
5. Peek

"""