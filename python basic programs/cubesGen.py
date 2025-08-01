def cubeGen(n):
    for i in range(1,n+1):
        yield i*i*i

for i in cubeGen(5):
    print(i)