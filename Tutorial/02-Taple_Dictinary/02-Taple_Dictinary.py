print "taple like list we cant change this list"
a = (1,2,3,4,5)
print a
#print a[0] = 1 error
print "get work , set not " + str(a[2])
print ""

print "tuple hold list and number we can insert number into the arrays but cant change the number :"
a = ([],100)
print str(a)
print str(a[0])
a[0].append(5)
a[0].append(6)
a[0].append(7)

print a[0]
print str(a[1])

#copy list
b = list(a)
print str(b)

print "Dictinary : "
c = {}
c["one"] = 1
c["two"] = 2

d = {}
d[1] = "one"
d[2] = "two"

print c
print d


print str(c.keys()) + " " + str(c.values())
c.__delitem__("one")
print str(c.keys()) + " " + str(c.values())

#if we dont do copy then two dictinary point to same dictinary
h = c.copy()


f = range(10) + range(10) + [5]

print f
y = {}

#for each
for i in f:
    if(y.has_key(i)):
        y[i]+=1
    else :
        y[i] = 1
print y

#from like java for
for i in range(len(f)):
    if(f[i] in f):
        y[f[i]]+=1
    else :
        y[f[i]] = 1

print y

#only keys not values
print 0 in y # map!!
print 1 in y
print 90 in y
print 8 in f
