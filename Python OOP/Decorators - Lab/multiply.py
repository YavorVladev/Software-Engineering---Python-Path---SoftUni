def multiply(times):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return result * times

        return wrapper

    return decorator
