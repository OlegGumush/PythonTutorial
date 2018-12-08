#pow function
def pw(x):
    return x**2

#pow lambda function
l = lambda x:x**2

print pw(10)
print l(5)

def sum(a,b):
    return a+b

a = lambda x,y:x+y

print sum(1,4)
print a(1,4)

#Must not define variables inside lambda, permitted only one expression. Expression can be very defficalt
#we can call function in lambda

f = lambda x,y:(x>5) or (x==2) or (x<1 and y==5)

print f(1,2)
print f(7,0)


f = lambda x,y:sum(x,y)
print f(1,3)





