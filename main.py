import UI.Interface
import Librar.data_collector
import Librar.wrapper


user_dat = Librar.data_collector.user_info_get()
cpu_dat = Librar.data_collector.cpu_get()
mem_dat = Librar.data_collector.memory_get()
boot_dat = Librar.data_collector.boot_get()
proc_dat = Librar.data_collector.info_apps_get()
title_name = "Task Manager"
num_running_apps = len([process for process in proc_dat
                        if process['status'] == 'running'
                        or process['status'] == 'idle'])


def main():
    UI.Interface.title_show(user_dat, title_name)
    UI.Interface.cpu_show(cpu_dat)
    UI.Interface.memory_show(mem_dat)
    UI.Interface.boot_show(*boot_dat)
    UI.Interface.process_list_show(proc_dat, num_running_apps)


if __name__ == "__main__":
    main()
