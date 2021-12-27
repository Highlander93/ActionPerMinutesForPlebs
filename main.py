import threading

import arrayhandler
import keyboardhandler
import mousehandler


def start_program():
    thread_keyboardhandler = threading.Thread(target=keyboardhandler.start_thread_keyboardhandler)
    thread_mousehandler = threading.Thread(target=mousehandler.start_thread_mousehandler)
    thread_arrayhandler = threading.Thread(target=arrayhandler.start_thread_arrayhandler)

    thread_keyboardhandler.start()
    thread_mousehandler.start()
    thread_arrayhandler.start()


if __name__ == '__main__':
    start_program()
