
print 'function without parameters'
def my_hi():
    print 'hi'
my_hi()

print 'function get variables'
def my_print(st):
    print st
my_print('hi')

print 'functions with check if a and b is the same variable'
def sum( a ,b ):
    if type(a) == type(b):
        return a + b
    return None

c = sum(1,2)
print c

print 'return two values and functions get default variables'
def two_returns(a=5,b=4):
    return a+b , a*b

c = two_returns(2,5)
#two kind of str
print 'sum is ' + str(c[0])
print 'multiply ' + c[1].__str__()

print 'default parameters like c++ , f return two values , a values enter to the list c'
c = two_returns()
print 'sum is ' + str(c[0])
print 'multiply ' + c[1].__str__()

print 'concatenation two strings'
def cat(a, c):
    return str(a) + str(c)
print cat('aa' , 2)


print 'return two values'
def two_returns1(a=5,b=4):
    return a+b , a*b

sum , mult = two_returns1()
print str(sum) +" " + str(mult)


print 'unpacking list'
def two_returns2(a,b,c):
    return a+b , a*c

lst = [1,2,3]

sum , mult = two_returns2(*lst)
print str(sum) +" " + str(mult)


print 'wild cards'
def myprint(*args):
    s =0
    for x in args:
        s += x
    return s

c = myprint(1,2,3,4,5,6,7,8,9,10)
print c

print 'same but we need to enter at least one number'
def myprint(num , *args):
    s =num
    if not args:
        return s
    for x in args:
        s += x
    return s

c = myprint(1,2,3,4,5,6,7,8,9,10)
print c

print 'first param is list and second is dictinary'
def myprint(*args , **kwargs):
    s =0
    if args:
        for x in args:
            s += x
    if kwargs :
        for x in kwargs:
            s += kwargs[x]
    return s

lst = range(10)
dic = {'one' : 1 ,'two' : 2 }

c = myprint(*lst , **dic)
print c


print 'python know how to take values becouse keys same as function variables name'
print 'work only with dictinary:'
def myprint(firstName, id, lastName):
   print '%s   %s   %s '%(firstName , id , lastName)

d = {'firstName' : 'oleg' ,  'id' : 319638490 ,'lastName' : 'Gumush' }
myprint(**d)


print 'always same list python save in memory'
def f(lst = []):
    lst.append(1)
    print lst

f() #[1]
f() #[1,1]
f() #[1,1,1]


print 'The best way to do what we wanted to do before'
def f(lst = None):
    if lst == None:
        lst = []
    else :
        lst.append(1)
        print lst
print "list " + str(f())
f([])
f([])
f([])