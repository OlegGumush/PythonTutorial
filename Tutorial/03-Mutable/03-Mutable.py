a = [1,2,3,4, "df" , [123]]
print (a[5])

print ("primiteves:")
a = 4
b = a
b = 7
print ("not equals " + str(a) + " " + b.__str__())
print ("not equals addr " + str(id(a)) + " " + str(id(b)))
print
#immutable
#1.code readabbiliuty
#2.threads
#3.map fix

key = 'a'
d = {key : 'value'}
#immutable we change key
key = 'change key'
print (d)
print
d[key] =  'value1'
print (d)


#mutable - advanted
#1. performance
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#copy long string :(
ss = s
s+= '2'

#if string be muttable we dont need to copy
print (s)
print (ss)

print
print ("arrays mutable:")
a = [1,2,3]
b = a
b[0] = 10
print ("equals " + str(a) + " " +str(b))
print ("equals addr " + str(id(a)) + " " + str(id(b)))

a = []
b = a

#function can change out string
def change_val(lst):
    lst.append("olegOlegOleg")

change_val(a)

print (str(a))
print (str(b))


a = (1,2,3)
b = a
#cant append becouse a taple
#b.append(4)


print
#how to add string correct
s= ''
for num in range(10):
    s += str(num)
print (s)

print

#how to add string correct
s= ''
#id change and we do copy each iteration
for num in range(10):
    print 'the id is '  , id(s) , s

print

s= []
for num in range(10):
    print 'the id is '  , id(s) , s
    s += str(num)

#best way to catanate strings
print ('num is ', ''.join(s))

print


a = [1,2]
import copy
b = copy.copy(a)
print (b)