from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"my_function ok\n")
                else:
                    print(f"my_function ok")

            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'my_function error: {e}, inputs: {args}, {kwargs}')
                else:
                    print(f'my_function error: {e}, inputs: {args}, {kwargs}')
                raise
            return result
        return wrapper
    return decorator



@log(filename='')
def func(x, y):
    return x+y

result = func(1, 2)
print(result)


