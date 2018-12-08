import threading , random

def Splitter(words):
    global x
    myList = words.split()
    newList = []
    while(myList):
        newList.append(myList.pop(  random.randrange(0 , len(myList))   ))
    print newList


if __name__ == '__main__' :
    sentance = 'I am a handsome beast'
    numOfThreads = 5
    threadList = []

    print 'Start threading '

    for i in range(numOfThreads) :
        t = threading.Thread(target = Splitter , args= (sentance,))
        t.start()
        threadList.append(t)

    for i in range(numOfThreads) :
        threadList[i].join()
    print 'main done'