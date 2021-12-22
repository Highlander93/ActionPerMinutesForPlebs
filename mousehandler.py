import mouse


counter = 0


def anything_is_clicked_on_mouse(event):
    if hasattr(event, 'button'):
        if event.event_type == 'down' or event.event_type == 'double':
            global counter
            counter += 1
            print(str(counter) + "Mouse pressed \n________________________________________________")


def start_thread_mousehandler():
    print("Hi?")
    mouse.hook(callback=anything_is_clicked_on_mouse)
    mouse.wait(None)
