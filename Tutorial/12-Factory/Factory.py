class Winter(object) :
    pass
class Summer(object) :
    pass
class Fall(object) :
    pass
class Spring(object) :
    pass


class SeasonFactory(object):
    SEASON = {'Winter' : Winter ,'Summer' : Summer ,'Fall' : Fall ,'Spring' : Spring }

    #overide new
    def __new__(cls , season):
        return SeasonFactory.SEASON[season]()

a = SeasonFactory('Winter')
print a

if isinstance(a , Winter):
    print 'Winter'