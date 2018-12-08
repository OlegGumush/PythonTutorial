a =5
print a
a = "oleg"
print a
#arr
a = [3,5,6]
a.append(7)
print a
#set
a = {3,5,6}
a.add(7)
print a

#empty Array / List
b = [1,2,3]
print "empty array"  + str(b)
print "len of array " + str(len(b))
b.append(7)
b.append(5)
b.append(6)
print "array"  + str(b)
b.sort()
print "sorted array"  + str(b)

c = range(10)
print c
print "print only even" + str(c[0:10:2])
print "print only even" + str(c[::2])
print "print only even" + str(c[0:8:2])
print "print only even" + str(c[-1:0:2])
print "last " + str(c[-1])
print "pre last " + str(c[-2])
print "pre pre last " + str(c[-3])
print "String :"


b.reverse() # return NONE
a = b.reverse()
print "a not reverse of b " + str(a)
print "reverse " + str(b)


print "c:\\"
print "not need two \\ " + r"c:\oleg"
print "oleg"
print '"oleg"'
print '''"ol,, eg"'''

e = "oleg"