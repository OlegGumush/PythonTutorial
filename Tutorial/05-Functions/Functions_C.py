import time

print 'calculate time'
def f():
    timeStart = time.time()
    time.sleep(1)
    print time.time() - timeStart
f()

print
def timeit(func):
    def cloc(*args , **kwargs):
        print 'args' , args
        print 'args' , kwargs
        print 'start timer'
        t0 = time.time()
        result = func(*args ,**kwargs)
        t1 = time.time()
        print 'end timer'
        print 'function ' , func.__name__ , '()' , 'took' , t1 - t0 , 'sec'
        return result
    return cloc

@timeit
def a(a,b,c):
    print 'start func a()'
    time.sleep(3)
    print 'end func a()'

a(1,2,3)

