#!/usr/bin/python

def fib(n):
    """print a fibonacci sequence up to n"""
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b

def getFib(n):
    """return the fibonacci sequence up to n"""
    a = [0, 1]
    while a[len(a)-1] < n:
        a.append(a[len(a)-1] + a[len(a)-2])
    return a

def func1(a, b = 1, c = "xyz"):
    if c in ("yes", "maybe", "never"):
        print "yeeessss"
    else:
        raise IOError("oh god")
    print "a = ", a, "b = ", b, "c = ", c

def func2(*a, **b):
    print "----"
    for i in a:
        print i
    print "----"
    for i in sorted(b.keys()):
        print i, " ",  b[i]

print "calling fib(1000)"
fib(1000)

print "calling a(20)"
a = fib
a(20)

print "calling getFib(100)"
print getFib(100)

# func1(10)
# func1(10, 20, 30)
func1(20, 30, "yes")
func1(10, c = "yes")

func2("abc", "zyx", a=10, b=20, c=30)

zzz = { "abc": "123", "zyx": "999" }
func2(**zzz)
