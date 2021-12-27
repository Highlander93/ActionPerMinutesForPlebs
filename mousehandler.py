from datetime import datetime

import mouse

import arrayhandler


def anything_is_clicked_on_mouse(event):
    if hasattr(event, 'button'):
        if event.event_type == 'down' or event.event_type == 'double':
            arrayhandler.write_action_in_arr()


def start_thread_mousehandler():
    mouse.hook(callback=anything_is_clicked_on_mouse)
    mouse.wait(None)
