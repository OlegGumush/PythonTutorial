print 'Python variables and functions must not be the same name'
print

print 'Python can identify variables defined before the function becouse x is global if we want use global x we define this in func'
print 'If you do not define it (x) as global in func, we can only global look at it but not change it or add to it in a function'
print 'python work with dictinary with globals'
print 'each function have his dictinary'

x = 90
def my_func():
    global x
    x += 10
    print 'x in func ' + str(x)

my_func()
print 'after func ' + str(x)

print
print 'funcs in fincs'

def f(param , n1 , n2) :
    if param == '+' :
        def f():
            print n1+n2
            return n1 + n2
    elif param == '*' :
        def f():
            print n1*n2
            return n1*n2
    return f()

temp = f('*' , 3 , 10)
print temp

print 'pass sintax - Not throwing error'

x = 7
if x > 5 :
    pass
else :
    pass

print

print 'math -- > in python no consts i can change pi not good !!!!'
import math
print 'PI ' + str(math.pi)
math.pi = 4
print 'PI ' + str(math.pi)

print

a=5
b =7

a , b=b , a
print 'switch'
print 'a' + str(a)
print 'b' + str(b)


print 'global list'

lst = []

def a():
    global lst
    lst += [2]

def b():
    global lst
    lst.append(3)

a()
b()

print lst