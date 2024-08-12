# from datetime import datetime
from typing import Callable, Any


def log(filename: Any = None) -> Callable:
    """Декоратор логирует работу функции, выводя данные в консоль или в файл, если он указан"""

    def my_decorator(func: Callable) -> Callable:
        '''Декоратор принимает в качестве аргумента декорируемую функцию'''
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # time_1 = datetime.now()
                result = func(*args, **kwargs)
                # time_2 = datetime.now()
                if filename:
                    with open(filename, "a") as file:
                        file.write("my_function ok\n")
                else:
                    print("my_function ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"my_function error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


@log()
def func(x, y):
    return x // y


result = func(4, 2)
print(result)
