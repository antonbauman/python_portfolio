# import pytz
from datetime import datetime

# Дата та час
def func_name_and_time(func):
    def wrapper(*args, **kwargs):
        # eu_KY = pytz.timezone('Europe/Kyiv')
        local = datetime.now()
        # current_time = datetime.now(eu_KY)
        current_time = local.strftime("%d/%m/%Y, %H:%M:%S")
        function_name = func.__name__
        print(f"Час виклику: {current_time} \n"
              f"Ім'я функції: {function_name}")
        return func(*args, **kwargs)
    return wrapper


@func_name_and_time
def first_name():
    print("Привіт, ти бачиш ім'я, час та дату виклику функції")

first_name()


print()

# Custom exception is occured
class MyCustomException(Exception):
    def __init__(self):
        self.message = "Custom exception is occured"

try:
    raise MyCustomException()
except MyCustomException as a:
    print(a.message)


print()

class MyContextManager:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print("An exception:", exc_val)
        print("=" * 10)
        return True

with MyContextManager():
    print("Some code")

print()

try:
    print("="*10)
    print("Some code")
    raise ValueError("Something wrong")
except Exception as e:
    print("An exception occurred:", e)
else:
    print("="*10)
finally:
    print("="*10)
