#1.Write a Python class that simulates a Stack. The class should implement 
#methods like push, pop, peek (the last two methods should return None if no
#element is present in the stack).
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if len(self.stack) == 0:
            return None     
        return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
s1 = Stack()
s1.push(1) 
s1.push(2)
s1.push(3)
s1.push(4)
#print(s1.peek())
#print(s1.stack)
s1.pop()
#print(s1.stack)
#print(s1.peek())

#2.Write a Python class that simulates a Queue. The class should implement 
#methods like push, pop, peek (the last two methods should return None if no 
#element is present in the queue).
class Queue:
    def __init__(self):
        self.queue = []
    def push(self, element):
        self.queue.append(element)
    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    
q1 = Queue()
q1.push(1)
q1.push(2)
q1.push(3)
q1.push(4)
#print(q1.peek())
#print(q1.queue)
q1.pop()
#print(q1.queue)


#3.Write a Python class that simulates a matrix of size NxM, with N and M 
#provided at initialization. The class should provide methods to access elements 
#(get and set methods) and some mathematical functions such as transpose, matrix 
#multiplication and a method that allows iterating through all elements from a 
#matrix an apply a transformation over them (via a lambda function)
class Matrix:
    def __init__(self, N, M):
        self.matrix = []
        self.n = N
        self.m = M
        for i in range(N):
            self.matrix.append([0]*M)
    def get(self, i, j):
        return self.matrix[i][j]
    def set(self, i, j, value):
        self.matrix[i][j] = value
    def transpose(self):
        return [[self.matrix[j][i] for j in range(self.n)] for i in range(self.m)]        
    def multiply(self, other):
        if self.m != other.n:
            return None
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result
    def apply(self, f):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = f(self.matrix[i][j])
    
    
m = Matrix(2, 2)
m1 = Matrix(2, 3)
m.set(0, 0, 1)
m.set(1, 1, 5)
print(m.matrix)
m1.set(0, 0, 2)
m1.set(1, 1, 3)
m1.set(1, 2, 4)
print(m1.matrix)
print(m.transpose())
print(m.multiply(m1).matrix)
m.apply(lambda x: x*2)
print(m.matrix)
        