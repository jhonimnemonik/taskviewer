import time


def title_show(user_info_list, title_name):
    button = "⊟ ⊡ ⊠ ╗"
    t_st = time.strftime
    t_gm = time.gmtime
    print(f'╔{title_name:═^104} {button:<7}')
    for u_name, u_time in user_info_list:
        print("║{:>90}{:<10}{:<10}║".format("", "User name: ", u_name))
        print("║{:>90}{:<10}{:<10}║".format("", "On system: ", t_st("%H:%M:%S", t_gm(u_time))))


def cpu_show(cpu_data):
    inf = cpu_data
    us_t = inf['user']
    sys_t = inf['system']
    perc = inf['percent']
    load = "{:░<10}".format("▓" * int(perc / 10))
    user_time = time.strftime("%H:%M:%S", time.gmtime(us_t))
    system_time = time.strftime("%H:%M:%S", time.gmtime(sys_t))
    print("║\t{:<10}{:<10}{:<10}{}{:<68}║".format("CPU", "Load:", str(perc)+" % ", load, ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("CPU time", "User:", str(user_time), ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "System:", str(system_time), ""))
    print("║{:<111}║".format(""))


def memory_show(mem_data):
    mem = mem_data
    perc = mem['percent']
    tot = mem['total'] // 1024 ** 2
    free = mem['free'] // 1024 ** 2
    bar = "{:░<10}".format("▓" * int(perc/10))
    print("║\t{:<10}{:<10}{:<10}{}{:<68}║".format("Ram", "Load:", str(perc) + " % ", bar, ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "Total:", str(tot) + " Mb.", ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "Free:", str(free) + " Mb.", ""))
    print("║{:<111}║".format(""))


def boot_show(boot_info):
    b_inf = boot_info
    print("║\t{:<15}{:<5}{:<30}{:<58}║".format("Boot time:", "", b_inf['boot_time'], ""))
    print("║\t{:<15}{:<5}{:<30}{:<58}║".format("Time since On:", "", b_inf['since_time'], ""))


def process_list_show(processes, num_apps):
    print("║\t{:<20}{:<88}║".format("Running app-s:", num_apps))
    print("║{:<111}║".format(""))
    print("╠{0:─^3}┬{0:─^64}┬{0:─^20}┬{0:─^5}┬{0:─^5}┬{0:─^9}╣".format("─"))
    print("║{:^3}│{:^64}│{:^20}│{:^5}│{:^5}│{:^9}║".format("№", "Name", "User", "%", "PID", "Status"))
    print("╠{0:─^3}┼{0:─^64}┼{0:─^20}┼{0:─^5}┼{0:─^5}┼{0:─^9}╣".format("─"))
    for p in processes:
        if p['username'] is not None:
            print(
                "║{:<3}│{:<64}│{:^20}│{:^5}│{:^5}│{:^9}║".format(
                    p['number'], p['name'],
                    p['username'], p['cpu_percent'],
                    p['pid'], p['status'])
            )
        else:
            print(
                "║{:<3}│{:<64}│{:^20}│{:^5}│{:^5}│{:^9}║".format(
                    p['number'], p['name'],
                    "None", p['cpu_percent'],
                    p['pid'], p['status'])
            )
    print("╚{0:═^3}╧{0:═^64}╧{0:═^20}╧{0:═^5}╧{0:═^5}╧{0:═^9}╝".format("═"))
