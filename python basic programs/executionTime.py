import time

def dec(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = func(*args , **kwargs)
        end_time = time.time()
        print("Execution time is :" , end_time-start_time)
        return result
    return wrapper

@dec
def add(a , b):
    for i in range(1,100):
        for j in range(i,100):
            for k in range(j,100):
                print(i+j+k)
    return a+b

add(4,5)