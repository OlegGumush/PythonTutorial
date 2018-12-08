import threading

def main() :

    print threading.active_count()
    print str(threading.enumerate())
    print str(threading.current_thread())




if __name__ == '__main__':
    main()
