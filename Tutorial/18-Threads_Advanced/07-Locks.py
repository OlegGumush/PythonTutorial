import threading

def do_thread():
    global x , first , second

    threading._sleep(3)
    first.acquire()
    try :
        while x < 300:
            x += 1
        print x
    finally:
        second.release()

def after_thread():
    global x , first , second

    second.acquire()
    try :
        while x < 600:
            x += 1
    finally:
        first.release()

    print x , " "

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
