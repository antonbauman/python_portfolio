import json
import datetime

phone_list = [
    ["Robb", "0680929258"],
    ["Stark", "380912146146"],
    ["Jonn", "+380636690103"],
    ["Snow", "+380638690261"],
    ["Tirion", "+958758767"]
]

def add_contact():
    # Відкриваємо файл телефонної книги
    with open("phone_list.json", "r") as f:
        phone_list = json.load(f)

    # Вводимо дані нового контакту
    name = input("Введіть ім'я контакту: ")
    phone = input("Введіть телефонний номер контакту: ")

    # Додаємо новий запис
    phone_list.append([name, phone])

    # Зберігаємо оновлену телефонну книгу у файл
    with open("phone_list.json", "w") as f:
        json.dump(phone_list, f)


add_contact()


def log_func_call(func):
    def wrapper(*args, **kwargs):
        with open("function_log.txt", "a") as f:
            f.write(f"Function '{func.__name__}' called at {datetime.datetime.now()}\n")
        return func(*args, **kwargs)

    return wrapper


@log_func_call
def my_function():
    print("Збережено назву та час виклику функції")


my_function()


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.datetime.now()
        with open("error_log.txt", "a") as f:
            f.write(f"Error occurred at {self.timestamp}: {self.message}\n")
        super().__init__(self.message)


raise MyCustomException("Some wrong")