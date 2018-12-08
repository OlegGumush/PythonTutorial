import threading

def do_thread():
    print "this is our thread!"

def main():

    out_thread = threading.Thread(target = do_thread())
    out_thread.start()

    print threading.active_count()
    print str(threading.enumerate())
    print str(threading.current_thread())


if __name__ == '__main__':
    main()
