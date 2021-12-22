import keyboard


counter = 0
arr = []


def anything_is_pressed_on_keyboard():
    global counter
    global arr
    counter += 1
    print(str(counter) + "Keyboard pressed \n________________________________________________")


def start_thread_keyboardhandler():
    keyboard.on_release(anything_is_pressed_on_keyboard, suppress=False)
    keyboard.wait()
