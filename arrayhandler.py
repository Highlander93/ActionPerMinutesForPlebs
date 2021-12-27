import datetime
import time

arr = []


def start_thread_arrayhandler():
    callback_to_check_arr()


def delete_old_actions():
    while arr[0] < (datetime.datetime.now()-datetime.timedelta(minutes=1)):
        arr.pop(0)
        if len(arr) < 1:
            break


def write_action_in_arr():
    arr.append(datetime.datetime.now())


def callback_to_check_arr():
    if len(arr) > 0:
        delete_old_actions()
    print(len(arr))
    time.sleep(1)
    callback_to_check_arr()
