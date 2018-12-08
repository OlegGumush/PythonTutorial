# need to add
import abc
print 'abstract classes , python not have interfaces'

class Base(object):
    #need to add
    __metaclass__ = abc.ABCMeta

    #need to implements in derived class
    @abc.abstractmethod
    def i_am(self):
        print 'i am base'

    def foo(self):
        print 'i am foo'

class Derived(Base):

    def i_am(self):
        print 'i am Derived'


d = Derived()
d.i_am()
d.foo()

########################################################################################################################

class Base2(object):
    #need to add
    __metaclass__ = abc.ABCMeta

    #old sintax to implements abstract class not good
    def i_am(self):
        raise Exception()

    def foo(self):
        print 'i am foo'

class Derived2(Base2):

    def i_am(self):
        print 'i am Derived'

b = Base2()
b.i_am()

d = Derived()
d.i_am()











































