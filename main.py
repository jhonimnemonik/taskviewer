from UI import Interface as view
from Librar import data_collector as dat


user_dat = dat.user_info_get
cpu_dat = dat.cpu_get
mem_dat = dat.memory_get
boot_dat = dat.boot_get
proc_dat: object = dat.info_apps_get()
title_name = "Task Manager"
num_running_apps = len([process for process in proc_dat
                        if process['status'] == 'running'
                        or process['status'] == 'idle'])


def main():
    view.title_show(user_dat, title_name)
    view.cpu_show(cpu_dat)
    view.memory_show(mem_dat)
    view.boot_show(*boot_dat())
    view.process_list_show(proc_dat, num_running_apps)


if __name__ == "__main__":
    main()
