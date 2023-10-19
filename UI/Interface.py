from time import strftime, gmtime


def title_show(user_info_list, title_name):
    button = "⊟ ⊡ ⊠ ╗"
    print(f"╔{title_name:═^104} {button:<7}")
    for user_name, user_time in user_info_list:
        print("║{:>90}{:<10}{:<10}║".format("", "User name: ", user_name))
        print("║{:>90}{:<10}{:<10}║".format("", "On system: ",
                                            strftime("%H:%M:%S", gmtime(user_time))))


def cpu_show(cpu_data):
    _times, percent = cpu_data
    load = "{:░<10}".format("▓" * int(percent / 10))
    user_time = strftime("%H:%M:%S", gmtime(_times.user))
    system_time = strftime("%H:%M:%S", gmtime(_times.system))
    print("║\t{:<10}{:<10}{:<10}{}{:<68}║".format("CPU", "Load:", str(percent) + " % ", load, ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("CPU time", "User:", str(user_time), ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "System:", str(system_time), ""))
    print("║{:<111}║".format(""))


def memory_show(mem_data):
    total, percent, free = mem_data
    load = "{:░<10}".format("▓" * int(percent / 10))
    print("║\t{:<10}{:<10}{:<10}{}{:<68}║".format("Ram", "Load:", str(percent) + " % ", load, ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "Total:", str(total // 1024 ** 2) + " Mb.", ""))
    print("║\t{:<10}{:<10}{:<10}{:<78}║".format("", "Free:", str(free // 1024 ** 2) + " Mb.", ""))
    print("║{:<111}║".format(""))


def boot_show(boot_time, since_time):
    print("║\t{:<15}{:<5}{:<30}{:<58}║".format("Boot time:", "", boot_time, ""))
    print("║\t{:<15}{:<5}{:<30}{:<58}║".format("Time since On:", "", since_time, ""))


def process_list_show(processes, num_apps):
    print("║\t{:<20}{:<88}║".format("Running app-s:", num_apps))
    print("║{:<111}║".format(""))
    print("╠{0:─^3}┬{0:─^64}┬{0:─^20}┬{0:─^5}┬{0:─^5}┬{0:─^9}╣".format("─"))
    print("║{:^3}│{:^64}│{:^20}│{:^5}│{:^5}│{:^9}║".format("№", "Name", "User", "%", "PID", "Status"))
    print("╠{0:─^3}┼{0:─^64}┼{0:─^20}┼{0:─^5}┼{0:─^5}┼{0:─^9}╣".format("─"))
    for process in processes:
        if process['username'] is not None:
            print(
                "║{:<3}│{:<64}│{:^20}│{:^5}│{:^5}│{:^9}║".format(
                    process['number'], process['name'],
                    process['username'], process['cpu_percent'],
                    process['pid'], process['status'])
            )
        else:
            print(
                "║{:<3}│{:<64}│{:^20}│{:^5}│{:^5}│{:^9}║".format(
                    process['number'], process['name'],
                    "None", process['cpu_percent'],
                    process['pid'], process['status'])
            )
    print("╚{0:═^3}╧{0:═^64}╧{0:═^20}╧{0:═^5}╧{0:═^5}╧{0:═^9}╝".format("═"))


