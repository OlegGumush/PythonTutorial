print 'sum'
list = [1,2,3,4,5]
list2 = [x+2 for x in list]

print list
print list2

print 'pow'
list = [1,2,3,4,5]
list2 = [x**2 for x in list]

print list
print list2

print 'mult'
list = [1,2,3,4,5]
list2 = [x*2 for x in list]

print list
print list2


print 'only even numbers'
list = range(100)
l2 = [x for x in list if x %2 ==0]
print l2

print '(zugot sdurim)'
list = [x+y for x in 'ABCD' for y in 'abcd']
print list