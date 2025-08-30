def log(filename=None):
    """декоратор с параметрами, который указывает, в какой файл записывать логи"""

    def actual_log(function):
        """основной декоратор, который в зависимости от присутствия файла в
        параметрах записывает результат в файл или выводит в консоль"""

        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{function.__name__} ok\n")
                else:
                    print(f"{function.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")

        return wrapper

    return actual_log


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


@log()
def new_func(x, y):
    return x - y