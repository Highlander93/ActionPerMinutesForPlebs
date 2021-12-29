import datetime
import time


all_actions_in_one_minute = []


def start_thread_arrayhandler():
    infinity_loop_to_check_and_delete_old_actions()


def delete_old_actions():
    while all_actions_in_one_minute[0] < (datetime.datetime.now()-datetime.timedelta(minutes=1)):
        all_actions_in_one_minute.pop(0)
        if len(all_actions_in_one_minute) < 1:
            break


def write_action_in_arr():
    all_actions_in_one_minute.append(datetime.datetime.now())


def infinity_loop_to_check_and_delete_old_actions():
    while True:
        if len(all_actions_in_one_minute) > 0:
            delete_old_actions()
        #print(len(all_actions_in_one_minute))
        time.sleep(1)


def get_length_array_apm_backend():
    return len(all_actions_in_one_minute)
