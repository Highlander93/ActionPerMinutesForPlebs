from datetime import datetime

import keyboard

import arrayhandler


def anything_is_pressed_on_keyboard(event):
    arrayhandler.write_action_in_arr()


def start_thread_keyboardhandler():
    keyboard.on_release(anything_is_pressed_on_keyboard, suppress=False)
    keyboard.wait()
