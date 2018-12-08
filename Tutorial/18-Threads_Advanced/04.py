import threading

dead = False

def do_thread():
    global dead
    print 'thread start function do thread' , threading.current_thread().name
    x = 0
    while not dead:
        x += 1

    print 'number of x ', x


def main():
    global dead

    dead = False

    out_thread = threading.Thread(target=do_thread , name = 'my_thread')
    out_thread.start()
    out_thread.join(1)

    print 'main thread'
    print 'our thread is Alive?' , out_thread.is_alive()

    raw_input("Hit enter to die")
    dead = True

    out_thread.join(1)
    print 'our thread is Alive?' ,out_thread.is_alive()


if __name__ == '__main__':
    main()