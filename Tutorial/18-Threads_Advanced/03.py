import threading

dead = False

def do_thread():
    global dead

    print "this is our thread!" , threading.current_thread()
    x =0
    while not dead :
        x+=1

    print threading.current_thread() , 'number of x ' , x

def main():
    global dead
    
    dead = False

    out_thread = threading.Thread(target = do_thread)
    out_thread.start()

    print 'main thread'
    print threading.active_count()
    print str(threading.enumerate())
    print str(threading.current_thread())

    raw_input("Hit enter to die")
    dead = True

if __name__ == '__main__':
    main()
