import random
def randGen(start , end):
    yield random.randint(start, end)


for i in range(10):
    start = int(input("Enter start :"))
    end = int(input("Enter end :"))
    for j in randGen(start,end):
        print(j)