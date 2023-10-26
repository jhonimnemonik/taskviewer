from functools import wraps
import json
import datetime
import os


def log_to_file(file_name: str):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = func(*args, **kwargs)
            output_dir = 'Logs'
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            file_path = os.path.join(output_dir, file_name + ".json")
            with open(file_path, 'a') as file:
                json.dump(dat_time, file)
                file.write("\n")
                json.dump(f"Get for: {func.__name__}", file)
                file.write("\n")
                for entry in result:
                    file.write(json.dumps(entry) + '\n')
            return result

        return wrapper

    return my_decorator
