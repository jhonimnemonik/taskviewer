from functools import wraps
import json
import datetime


def log_to_file() -> object:
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = func(*args, **kwargs)
            file_name = func.__name__ + '_log.json'
            with open(file_name, 'a') as file:
                json.dump(dat_time, file)
                file.write("\n")
                json.dump(f"Get for: '{func.__name__}'", file)
                file.write("\n")
                json.dump(f"Info: {result}", file)
                file.write("\n\n")
            return result

        return wrapper

    return my_decorator
