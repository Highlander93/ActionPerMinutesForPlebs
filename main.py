import threading

import keyboardhandler
import mousehandler


def start_program():
    thread_keyboardhandler = threading.Thread(target=keyboardhandler.start_thread_keyboardhandler)
    thread_mousehandler = threading.Thread(target=mousehandler.start_thread_mousehandler)

    thread_keyboardhandler.start()
    thread_mousehandler.start()


if __name__ == '__main__':
    start_program()

