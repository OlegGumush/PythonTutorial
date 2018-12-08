import random

lst = range(20)
random.shuffle(lst)

print lst

#return None
lst.sort()
print lst

#return sorted list and not sorted the list
print sorted(lst)

print 'sort reverse'
#sort reverse
lst.sort(None , None , True)
print lst

#comparator
print 'comparator example'
class Person(object):
    def __init__(self , name):
        self.name = name

    def __str__(self):
        return  str(self.name)

a4 = Person('a')
a1 = Person('bb')
a2 = Person('ccc')
a3 = Person('dddd')

lst = []
lst.append(a1)
lst.append(a2)
lst.append(a3)
lst.append(a4)

def cmp1(a,b) :
    if (a.name > b.name ) :
        return 1
    elif (a.name < b.name):
        return -1
    else :
        return 0

print 'do nothing need comparator' + str([str(x) for x in sorted(lst , cmp1)])

################################################################################################
#key return value of number or string
#key better than cmp

lst.sort(key = lambda x : x.name )
print [str(x) for x in lst]


lst.sort(key = lambda x : len(x.name) , reverse=True )
print [str(x) for x in lst]

