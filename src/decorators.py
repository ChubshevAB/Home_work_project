from functools import wraps


def log(filename=None):
    """Функция-декоратор логирует работу функции и выводит сообщение о успешной работе либо об ошибке в консоль либо в файл, если указать имя файла"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function ok\n")
                else:
                    print(f"my_function ok")

            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}, inputs: {args}, {kwargs}")
                else:
                    print(f"my_function error: {e}, inputs: {args}, {kwargs}")
                raise
            return result

        return wrapper

    return decorator


@log(filename="")
def func(x, y):
    return x + y


result = func(1, 2)
print(result)
