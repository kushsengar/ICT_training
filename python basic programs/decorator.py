def dec(func):
    def wrapper():
        return func+2
    return wrapper

@dec
def add():
    return 5

print(add())