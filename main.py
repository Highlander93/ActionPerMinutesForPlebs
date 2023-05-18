import threading
import tools.constants

from Backend import mousehandler, keyboardhandler, arrayhandler
from Frontend import windowhandler


def start_program():
    thread_keyboardhandler = threading.Thread(target=keyboardhandler.start_thread_keyboardhandler)
    thread_mousehandler = threading.Thread(target=mousehandler.start_thread_mousehandler)
    thread_arrayhandler = threading.Thread(target=arrayhandler.start_thread_arrayhandler)
    thread_windowhandler = threading.Thread(target=windowhandler.start_window)

    thread_keyboardhandler.start()
    thread_mousehandler.start()
    thread_arrayhandler.start()
    thread_windowhandler.start()


if __name__ == '__main__':
    start_program()
