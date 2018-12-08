print 'filter'

def a(x):
    return x>5
lst = range(10)

c = filter(a,  lst)
b= filter(lambda x: x>5,  lst)

print b
print c
print
###########################################################

lst = range(20)
def a(x):
    return x >5 and x%2 ==0

b = filter(lambda x: x >5 and x%2 ==0 , lst)
c = filter(a , lst)

print b
print c
print

#############################################################
#list commprehention
print [x for x in range(20) if x >5 and x%2 ==0 ]
print


print 'Map'

print map(lambda x : x**2 , range(10))
print map(lambda x , y: x+y  , range(10) , range(10))
print [x + y  for x in range(10)  for y in range(10) if x==y]


























