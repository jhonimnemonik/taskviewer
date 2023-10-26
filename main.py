from Librar import data_collector as dc
from Ui import Interface as iu

user_dat = dc.user_info_get()
cpu_dat = dc.cpu_get()
mem_dat = dc.memory_get()
boot_dat = dc.boot_get()
proc_dat = dc.info_apps_get()
title_name = "Task Manager"
num_running_apps = len([process for process in proc_dat
                        if process['status'] == 'running'
                        or process['status'] == 'idle'])


def main():
    iu.title_show(user_dat, title_name)
    iu.cpu_show(cpu_dat)
    iu.memory_show(mem_dat)
    iu.boot_show(boot_dat)
    iu.process_list_show(proc_dat, num_running_apps)


if __name__ == "__main__":
    main()
