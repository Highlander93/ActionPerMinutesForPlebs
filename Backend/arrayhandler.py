import datetime
import time


all_actions_in_one_minute = []
max_apm = 0
total_actions = 0


def start_thread_arrayhandler():
    infinity_loop_to_check_and_delete_old_actions()


def delete_old_actions():
    while all_actions_in_one_minute[0] < (datetime.datetime.now()-datetime.timedelta(minutes=1)):
        all_actions_in_one_minute.pop(0)
        global total_actions
        total_actions += 1
        if len(all_actions_in_one_minute) < 1:
            break


def write_action_in_arr():
    all_actions_in_one_minute.append(datetime.datetime.now())


def infinity_loop_to_check_and_delete_old_actions():
    while True:
        if len(all_actions_in_one_minute) > 0:
            delete_old_actions()
        time.sleep(1)


def get_length_array_apm_backend():
    global max_apm
    if len(all_actions_in_one_minute) > max_apm:
        max_apm = len(all_actions_in_one_minute)
    return len(all_actions_in_one_minute)


def get_total_actions():
    global total_actions
    return total_actions + len(all_actions_in_one_minute)
