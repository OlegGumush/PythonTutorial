
if 3 > 2 :
    print True
elif 3 <2 :
    print True
else :
    print 'equals'

#&& = and   || = or
if 3>1 and 2 >1 or 4 >6 :
    print True

#regular for
for elem in [1,2,3]:
    print elem


#for else exist only in python
for elem in [1,2,3]:
    if elem == 4 :
        print 'Found'
        break
else:
    print 'not found'


#input
a = range(10) # a = [1,2,3...,10]
c = 5 #input('please enter a number ')

#for else exist only in python
for elem in a:
    if elem == c :
        print 'Found '
        break
else:
    print 'not found '


#while loop
a = range(5)
while a :
    print a.pop()





print

a = range(5)
b = range(7)

#i in a j in b print couples we run until the shortest array end
for i , j in zip(a,b):
    print i , j


# _ = zevel variable
for _ in range(len(a)):
    print a.pop()

a = range(5)

size = len(a)
for i in range(size):
    print i

print a

for e in a :
    if 2<e<4:
        del a[a.index(e)]
print a

#dictinary
d = {}
d['one'] = 1
d['two'] = 2
d['three'] = 3

#only keys
for key in d :
    print key
    print d[key] # values

#only values
for val in d.values() :
    print val

#couples
for key , val in d.items():
    print key , val