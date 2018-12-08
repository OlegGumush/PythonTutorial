class Person(object) :

    NUM_OF_INS =0

    def __init__(self , _name , _last , _age):
        #print '__init__ like ctor'
        #print 'define members in place'
        self.__name = _name
        self._last = _last
        self.age  = _age
        #not good !!!!  -- > self.NUM_OF_INS +=1
        Person.NUM_OF_INS += 1

    def __str__(self):
        return "" + str(self.__name) + " " +  str(self._last) + " " + str(self.age)

    #static method
    @staticmethod
    def static_method():
        print 'i am static'

    #class methon can only perrmision to static variables , convension get var cls
    #not has permission to members
    @classmethod
    def get_num_of_people(cls):
        print 'num of instances ' , cls.NUM_OF_INS

#def static_method():
#    print 'i am static'

l = []
for _ in range(10):
    l.append(Person(1,2,3))


print 'static arg'
print Person.NUM_OF_INS
print l[1].NUM_OF_INS
print l[3].NUM_OF_INS
print
print

print 'We think we changed it a value, but actually add it a mamber '
print 'Python will not up scope and therefore do not reach a static variable'
l[1].NUM_OF_INS = 1
print 'class name ' , Person.NUM_OF_INS
print 'instance   ' , l[1].NUM_OF_INS

print
print '''check static method , It does not mean that she was in class we'd rather spend it out '''
l[1].static_method()
