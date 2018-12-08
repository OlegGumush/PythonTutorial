print 'Group does not duplicates  not Sorted'
print 'operators work only if l1 l2 are sets'
s = set(range(10) + range(10))
print s
print range(10) + range(10)
print 'mutable like pointer'
b =s
b.add(44)
print s

print 'union'
s1 = set(range(5))
s2 = set(range(5,7))

print s1
print s2

s3 = s1.union(s2)
print s3
s3 = s1 | s2
print s3

print 'difference'
s1 = set(range(5))
s2 = set(range(2,7))

print s1
print s2

s3 = s1.difference(s2)
print s3
s3 = s1 - s2
print s3

print 'intersection'
s1 = set(range(5))
s2 = set(range(2,7))

print s1
print s2

print 'same vars in two lists'

lis1 = range(10)
lis2 = range(5,15)

print lis1
print lis2

print (set(lis1).intersection(lis2))
