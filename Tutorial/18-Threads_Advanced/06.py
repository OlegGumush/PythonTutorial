import threading

def do_thread():
    global x
    while x < 300:
        x += 1

    print x , " "

def after_thread():
    global x
    while x < 600:
        x += 1

    print x , " "

def main():

    global x
    x =0

    out_thread = threading.Thread(target=do_thread)
    out_thread.start()

    #302 600 we want to wait first thread


    out_thread1 = threading.Thread(target=after_thread)
    out_thread1.start()

    out_thread.join()
    out_thread1.join()

if __name__ == '__main__':
    main()
