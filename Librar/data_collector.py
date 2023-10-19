import psutil
import datetime
from Librar import wrapper


@wrapper.log_to_file("User log")
def user_info_get():
    user_info_list = []
    users = psutil.users()
    for user in users:
        name = user.name
        session_time = user.started
        user_info_list.append((name, session_time))
    return user_info_list


@wrapper.log_to_file("Cpu log")
def cpu_get():
    _times = psutil.cpu_times()
    percent = psutil.cpu_percent(interval=0)
    return _times, percent


@wrapper.log_to_file("Memory log")
def memory_get():
    mem_info = psutil.virtual_memory()
    total = mem_info.total
    percent = mem_info.percent
    free = mem_info.available
    return total, percent, free


@wrapper.log_to_file("Boot log")
def boot_get():
    time_value = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(time_value).strftime("%Y-%m-%d %H:%M:%S")
    since_time = "{:.0f}".format(time_value / 3600) + ' H.'
    return boot_time, since_time


@wrapper.log_to_file("Apps log")
def info_apps_get():
    process_info = []
    for number, proc in enumerate(psutil.process_iter(['name', 'pid', 'status', 'username', 'cpu_percent']), start=1):
        info = proc.as_dict(['name', 'pid', 'status', 'username', 'cpu_percent'])
        (process_info.append
            (dict(number=number, name=info.get('name'), pid=info.get('pid'), status=info.get('status'),
                  username=info.get('username'), cpu_percent=info.get('cpu_percent'))))
    return process_info
