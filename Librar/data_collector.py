import psutil
import datetime
from Librar import wrapper as wr


@wr.log_to_file("User")
def user_info_get():
    user_info = []
    users = psutil.users()
    for user in users:
        name = user.name
        session_time = user.started
        user_info.append((name, session_time))
    return user_info


@wr.log_to_file("CPU")
def cpu_get():
    times = psutil.cpu_times()
    percent = psutil.cpu_percent(interval=0)
    cpu_dict = {
        'user': times.user,
        'system': times.system,
        'percent': percent
    }
    return cpu_dict


@wr.log_to_file("Memory")
def memory_get():
    mem_info = psutil.virtual_memory()
    total = mem_info.total
    percent = mem_info.percent
    free = mem_info.available
    mem_list = {
        'total': total,
        'percent': percent,
        'free': free
    }
    return mem_list


@wr.log_to_file("Boot")
def boot_get():
    time_value = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(time_value).strftime("%Y-%m-%d %H:%M:%S")
    since_time = "{:.0f}".format(time_value / 3600) + ' H.'
    boot_list = {
        'boot_time': boot_time,
        'since_time': since_time,
    }
    return boot_list


@wr.log_to_file("Applications")
def info_apps_get():
    process_info = []
    for number, proc in enumerate(psutil.process_iter(['name', 'pid', 'status', 'username', 'cpu_percent']), start=1):
        info = proc.as_dict(['name', 'pid', 'status', 'username', 'cpu_percent'])
        process_info.append({
            'number': number,
            'name': info.get('name'),
            'pid': info.get('pid'),
            'status': info.get('status'),
            'username': info.get('username'),
            'cpu_percent': info.get('cpu_percent')
        })
    return process_info
