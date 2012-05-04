#!/usr/bin/python

a = []
a.append(10)
print a
a.extend([20, 30])
print a
a.insert(1, 99)
print a
a.remove(10)
print a
print a.pop()
print a.pop(1)
print a

a.extend([100000, 101, 102])
print a
print a.index(99)

print "a.count(100): ", a.count(100)
a.sort()
print "sorted: ", a
a.reverse()
print "reversed: ", a

stack = [0, 1, 2]
stack.append(99)
stack.append(1000)

print "stack: ", stack
print "stack.pop(): ", stack.pop()
print "stack.pop(): ", stack.pop()
print "stack: ", stack

queue = [0, 1, 2, 3, 5]
print "queue: ", queue
queue.insert(0, 99)
print "queue: ", queue
queue.insert(0, 100)
print "queue: ", queue
print "queue.pop(): ", queue.pop()
print "queue.pop(): ", queue.pop()
print "queue: ", queue

print "-----"

from collections import deque
queue = deque([1, 2, 3, 4, 6])
queue.append(10)
queue.append(20)
print "deque: ", queue
print "deque.popleft(): ", queue.popleft()
print "deque.popleft(): ", queue.popleft()
print "deque: ", queue

def f(x): return x % 2

print filter(f, range(1,30))

def g(x): return x*x

print map(g, range(1,10))

def h(x, y): return x*(y*y)

print map(h, range(1,10), range(1,10))

def reduce_test(x, y): return x+y
print reduce(reduce_test, range(1,10))

ss = [x**2 for x in range(10)]
print ss
ss = map(lambda x: x**3, range(10))
print ss

ss = [x*x for x in range(20) if x % 2]
print ss

s = [(x, x*y*z) for x in range(20) for y in range(20) for z in range(20) if x == y and y == z]
print s

sss = [x for (x,y) in s if y < 100]
print sss
sss = filter(lambda (x,y): y < 100, s)
print sss

matrix = [[10, 20, 30], [20, 30, 40], [100, 200, 300]]

print matrix
print [[row[i]*2  for row in matrix] for i in range(3)]
