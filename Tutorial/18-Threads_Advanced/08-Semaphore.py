import threading

def do_thread():
    global x , first , second


    while x < 300:
        first.acquire()
        print 'first ' , x
        x+=1
        second.release()


def after_thread():
    global x, first, second


    while x < 300:
        second.acquire()
        print 'two ' , x
        x+=1
        first.release()

def main():

    global x , first , second
    x =0
    first = threading.Semaphore(1)
    second = threading.Semaphore(0)

    x = 0

    out_thread = threading.Thread(target=do_thread)
    out_thread.start()

    out_thread1 = threading.Thread(target=after_thread)
    out_thread1.start()

    out_thread.join()
    out_thread1.join()

if __name__ == '__main__':
    main()
