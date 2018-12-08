from collections import namedtuple

person = namedtuple('my_person_tuple' , 'first last age gender')

jhon = person('oleg' , 'smith' , 26 , 1)
print jhon
print jhon.age
print jhon.first
#tuple we cant change
#jhon.age = 34

a = ['first','last','age','gender']
person = namedtuple('my_person_tuple' , a)
jhon = person('oleg' , 'smith' , 26 , 1)
print jhon
print jhon.age
print jhon.first
#tuple we cant change
#jhon.age = 34