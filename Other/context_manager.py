from contextlib import contextmanager


class MyContextManager:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, ex_type, value, traceback):
        self.file_obj.close()


@contextmanager
def context_manager_as_function(name, method):
    f = open(name, method)
    try:
        yield f
    except Exception as ex:
        print(ex)
    finally:
        f.close()


if __name__ == "__main__":
    with context_manager_as_function("test.txt", "r") as test:
        print(test.read())
        raise RuntimeError("Ba dum tss")
