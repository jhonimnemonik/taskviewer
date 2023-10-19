from functools import wraps
import json
import datetime


# def log_to_file(file_name) -> object:
#     def my_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             result = func(*args, **kwargs)
#             with open(file_name, 'a') as file:
#                 file.write(json.dump(dat_time, file, "\n"))
#
#                 # json.dump(f"Get for: '{func.__name__}'", file)
#                 # file.write("\n")
#                 # json.dump(f"Info: {result}", file)
#                 # file.write("\n\n")
#             return result
#
#         return wrapper
#
#     return my_decorator


def log_to_file(file_name):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = func(*args, **kwargs)
            with open(file_name+".json" , 'a') as file:
                json.dump(dat_time + "\n")
                json.dump("Get for: "+func.__name__+"\n")
                json.dump("Info: {result}\n\n")
            return result

        return wrapper

    return my_decorator
