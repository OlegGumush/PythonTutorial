#inheritance from object
class Person(object):

    def __init__(self , _name , _last , _age):
        print '__init__ like ctor'
        print 'define members in place'
        self.name = _name
        self.last = _last
        self.age  = _age

    def __str__(self):
        return "" + str(self.name) + " " +  str(self.last) + " " + str(self.age)

    def happy_bith(self):
        self.age +=1

p = Person('jhon' , 'smith' , 31)
print p
print dir(p)
print
p = Person('jhon' , 'smith' , '33')
print p
print

p.age = 50
p.name = 'oleg'
p.last = 'gumush'

print p
p.happy_bith()
print p

print 'add var to class person in run time not gooodddd!!!!'
p.salary = 10000
print p.salary

########################################################################################################################
#python function
#__name__

#only recomendation
#name - public
#_name - protected
#__name - private
print
print
########################################################################################################################

class Person1(object):

    def __init__(self , _name , _last , _age):
        print '__init__ like ctor'
        print 'define members in place'
        self.__name = _name
        self._last = _last
        self.age  = _age

    def __str__(self):
        return "" + str(self.__name) + " " +  str(self._last) + " " + str(self.age)

    def happy_bith(self):
        self.age +=1

p = Person1('jhon' , 'smith' , 31)
p.__name = 'oleg'
print str(p) + "---> name not changed because __name is like private do dir(p) and see the sintax"
print dir(p)
print 'change private'
p._Person1__name = 'oleg'
print str(p) + "---> name changed because _Person__name is the correct name of __name this sintax save as in inheritance"

print 'locals'
print locals()
print

print 'if we do import functions like _F() not pass otomaticaly'
print 'from Objects import * function like _f() not passed'
print 'from Objects import _f() , now _f() passed '
print 'Objects._f() , now _f() passed and we can use'
print 'not reccomended'
print
print

print "inheritance:"
class Worker(Person) :
    def __init__(self , name , last , age , salary):
        super(Worker,self).__init__(name , last , age)
        self.salary = salary

    def __str__(self):
        return super(Worker , self ).__str__() + " " + str(self.salary)

    def get_raise(self , bonus):
        self.salary += bonus

w = Worker('jhon' , 'smith' , 31 , 1000)
print w
w.get_raise(1000)
print w

print
print 'try catch'
try :
    w.stam()
except :
    print 'not good'

print
########################################################################################################################
print 'Multiple inheritance'
print



class Skill (object) :
    def __init__(self , skill_name):
        self.skill_name = skill_name

class Worker(Person ,Skill):
    def __init__(self , name , last , age , salary , skill_name):
        Person.__init__(self , name , last , age)
        Skill.__init__(self , skill_name)
        self.salary = salary

    def __str__(self):
        return super(Worker , self).__str__() + " " + str(self.salary) + " " + str(self.skill_name)

w = Worker('jhon' , 'smith' , 31 , 1000 , 'wow Skill')
print w











