import threading , random ,time

try :
    import Queue
except :
    import queue as Queue


class Producer(object):

    def __init__(self):
        self.food = ['ham' , 'salad' , 'soup']

    def run(self):
        global q

        for i in range(13) :
            f = self.food[random.randrange(len(self.food))]
            q.put(f)
            threading._sleep(1)
            print 'adding food to the queue'


class Consumer(object):

    def __init__(self):
        pass

    def run(self):
        global q

        for i in range(13) :

            if not q.empty():
                f = q.get()
            threading._sleep(1)
            print 'removing food to the queue ' , f


if __name__ == '__main__' :
    q = Queue.Queue(10)

    p = Producer()
    c = Consumer()

    pt = threading.Thread(target = p.run , args = ())
    ct = threading.Thread(target = c.run , args = ())

    pt.start()
    ct.start()
